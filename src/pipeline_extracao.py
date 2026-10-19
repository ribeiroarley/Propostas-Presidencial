"""Pipeline Modular de Extração Temática e Análise Comparativa (TSE).
Processa os planos de governo de Lula (PT) e Flávio (PL) em formato PDF,
classificando evidências textuais nos 7 macroeixos temáticos e exportando
para JSON e Markdown em outputs/.
"""

import sys
import os
import re
import json
import argparse
from pathlib import Path
import pymupdf
from rich.console import Console

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

console = Console()

# Definição dos 7 eixos temáticos e seus termos-âncora
TAXONOMIA_TEMAS = {
    "Economia e Finanças Públicas": [
        "fiscal", "orçamento", "reforma tributária", "inflação", "dívida", 
        "imposto", "arrecadação", "teto de gastos", "gastos públicos", 
        "câmbio", "banco central", "investimento", "produtividade"
    ],
    "Saúde": [
        "sus", "saúde", "atenção básica", "hospitais", "médicos", 
        "vacinas", "medicamentos", "filas de cirurgia", "telessaúde", 
        "saúde mental", "saneamento"
    ],
    "Educação": [
        "educação", "escola", "professores", "ensino fundamental", 
        "ensino médio", "universidade", "ensino superior", "creche", 
        "merenda", "alfabetização", "formação técnica", "pesquisa"
    ],
    "Segurança Pública": [
        "segurança pública", "polícia", "criminalidade", "homicídios", 
        "sistema penitenciário", "narcotráfico", "fronteiras", "armas", 
        "inteligência policial", "violência", "facções"
    ],
    "Agronegócio e Meio Ambiente": [
        "agro", "agronegócio", "agricultura familiar", "safra", "crédito rural", 
        "desmatamento", "meio ambiente", "sustentabilidade", "transição ecológica", 
        "recursos hídricos", "biodiversidade", "crédito de carbono"
    ],
    "Infraestrutura, Energia e Logística": [
        "infraestrutura", "logística", "transportes", "rodovias", "ferrovias", 
        "portos", "aeroportos", "energia elétrica", "concessões", "ppp", 
        "petróleo", "gás natural", "transição energética", "energia solar"
    ],
    "Assistência Social e Mercado de Trabalho": [
        "transferência de renda", "pobreza", "extrema pobreza", "assistência social", 
        "fome", "emprego", "salário mínimo", "direitos trabalhistas", 
        "seguridade social", "inclusão produtiva"
    ]
}

def extrair_texto_pdf(caminho_pdf: Path) -> list[dict]:
    """Extrai texto página por página preservando a rastreabilidade."""
    if not caminho_pdf.exists():
        raise FileNotFoundError(f"Arquivo não localizado: {caminho_pdf}")
        
    doc = pymupdf.open(caminho_pdf)
    paginas = []
    for num_pag in range(len(doc)):
        pagina = doc[num_pag]
        texto = pagina.get_text("text")
        texto_limpo = re.sub(r'\n+', '\n', texto).strip()
        paginas.append({
            "pagina": num_pag + 1,
            "conteudo": texto_limpo
        })
    doc.close()
    return paginas

def classificar_paragrafos(paginas: list[dict]) -> dict:
    """Distribui blocos textuais nos 7 eixos temáticos."""
    propostas_por_tema = {tema: [] for tema in TAXONOMIA_TEMAS.keys()}
    propostas_por_tema["Outros / Eixos Transversais"] = []

    for item in paginas:
        pagina_num = item["pagina"]
        texto = item["conteudo"]
        
        blocos = [b.strip() for b in texto.split("\n\n") if len(b.strip()) > 35]

        for bloco in blocos:
            bloco_lower = bloco.lower()
            alocado = False
            
            for tema, termos in TAXONOMIA_TEMAS.items():
                if any(re.search(rf"\b{re.escape(termo)}\b", bloco_lower) for termo in termos):
                    propostas_por_tema[tema].append({
                        "pagina": pagina_num,
                        "texto": bloco
                    })
                    alocado = True
                    break
            
            if not alocado and len(bloco) > 100:
                propostas_por_tema["Outros / Eixos Transversais"].append({
                    "pagina": pagina_num,
                    "texto": bloco
                })

    return propostas_por_tema

def gerar_markdown_tematico(dados: dict, caminho_saida: Path):
    """Gera sumário em Markdown das propostas classificadas."""
    with open(caminho_saida, "w", encoding="utf-8") as f:
        f.write("# Dados Extraídos por Eixo Temático (TSE)\n\n")
        f.write("> **Documento Intermediário:** Base de evidências textuais para auditoria e análise comparativa.\n\n")
        
        for tema in TAXONOMIA_TEMAS.keys():
            f.write(f"## 📌 Eixo Temático: {tema}\n\n")
            
            f.write("### Proposta: Lula\n")
            itens_lula = dados["candidatos"]["Lula"].get(tema, [])
            if itens_lula:
                for item in itens_lula[:10]:
                    f.write(f"- *(Pág. {item['pagina']})* {item['texto']}\n\n")
            else:
                f.write("_Nenhuma menção explícita direta localizada nos termos analisados._\n\n")
            
            f.write("### Proposta: Flávio\n")
            itens_flavio = dados["candidatos"]["Flávio"].get(tema, [])
            if itens_flavio:
                for item in itens_flavio[:10]:
                    f.write(f"- *(Pág. {item['pagina']})* {item['texto']}\n\n")
            else:
                f.write("_Nenhuma menção explícita direta localizada nos termos analisados._\n\n")
            
            f.write("---\n\n")

def executar_pipeline(caminho_lula: Path, caminho_flavio: Path, pasta_saida: Path):
    """Executa a rotina integral de parsing, estruturação e exportação."""
    pasta_saida.mkdir(parents=True, exist_ok=True)
    
    console.print(f"[bold green][*] Extraindo PDF Lula:[/bold green] {caminho_lula}")
    paginas_lula = extrair_texto_pdf(caminho_lula)
    lula_classificado = classificar_paragrafos(paginas_lula)

    console.print(f"[bold green][*] Extraindo PDF Flávio:[/bold green] {caminho_flavio}")
    paginas_flavio = extrair_texto_pdf(caminho_flavio)
    flavio_classificado = classificar_paragrafos(paginas_flavio)

    resultado_final = {
        "metadata": {
            "total_paginas_lula": len(paginas_lula),
            "total_paginas_flavio": len(paginas_flavio)
        },
        "candidatos": {
            "Lula": lula_classificado,
            "Flávio": flavio_classificado
        }
    }

    arquivo_json = pasta_saida / "extracao_tematica.json"
    with open(arquivo_json, "w", encoding="utf-8") as f:
        json.dump(resultado_final, f, ensure_ascii=False, indent=2)

    arquivo_md = pasta_saida / "extracao_tematica.md"
    gerar_markdown_tematico(resultado_final, arquivo_md)

    console.print(f"[bold cyan][✓] Pipeline concluído com sucesso![/bold cyan]")
    console.print(f"[✓] Arquivos gerados em: outputs/{arquivo_json.name} e outputs/{arquivo_md.name}")

def main():
    raiz_projeto = Path(__file__).resolve().parent.parent
    
    parser = argparse.ArgumentParser(description="Pipeline de extração temática de planos de governo.")
    parser.add_argument("--lula", type=Path, default=raiz_projeto / "data" / "lula.pdf", help="Caminho do PDF de Lula")
    parser.add_argument("--flavio", type=Path, default=raiz_projeto / "data" / "flavio.pdf", help="Caminho do PDF de Flávio")
    parser.add_argument("--output", type=Path, default=raiz_projeto / "outputs", help="Diretório de saída")
    args = parser.parse_args()

    executar_pipeline(args.lula, args.flavio, args.output)

if __name__ == "__main__":
    main()
