"""Script de extração e processamento automatizado dos Planos de Governo Presidenciais (TSE).
Processa os documentos 'proposta-pl.pdf' (Flávio Bolsonaro) e 'proposta-pt.pdf' (Luiz Inácio Lula da Silva)
para indexação temática, contagem léxica e análise fiscal/macroeconômica.
"""

import sys
import re
from pathlib import Path
import pypdf

def extrair_metadados_e_conteudo(caminho_pdf: Path):
    if not caminho_pdf.exists():
        raise FileNotFoundError(f"Arquivo {caminho_pdf} não encontrado.")
    
    leitor = pypdf.PdfReader(str(caminho_pdf))
    total_paginas = len(leitor.pages)
    
    conteudo_por_pagina = {}
    for idx, pagina in enumerate(leitor.pages):
        texto = pagina.extract_text() or ""
        conteudo_por_pagina[idx + 1] = texto
        
    return {
        "arquivo": caminho_pdf.name,
        "total_paginas": total_paginas,
        "conteudo": conteudo_por_pagina
    }

def analisar_termos_chave(dados: dict, termos: list):
    frequencias = {termo: 0 for termo in termos}
    paginas_por_termo = {termo: [] for termo in termos}
    
    for pag, texto in dados["conteudo"].items():
        for termo in termos:
            ocorrencias = len(re.findall(rf"\b{re.escape(termo)}\b", texto, re.IGNORECASE))
            if ocorrencias > 0:
                frequencias[termo] += ocorrencias
                paginas_por_termo[termo].append(pag)
                
    return frequencias, paginas_por_termo

def main():
    diretorio = Path(__file__).parent
    pdf_pl = diretorio / "proposta-pl.pdf"
    pdf_pt = diretorio / "proposta-pt.pdf"
    
    print(f"[+] Iniciando extração e análise textual via Python {sys.version.split()[0]}...")
    
    dados_pl = extrair_metadados_e_conteudo(pdf_pl)
    dados_pt = extrair_metadados_e_conteudo(pdf_pt)
    
    print(f"-> Proposta PL ({dados_pl['arquivo']}): {dados_pl['total_paginas']} páginas processadas.")
    print(f"-> Proposta PT ({dados_pt['arquivo']}): {dados_pt['total_paginas']} páginas processadas.")
    
    termos_fiscal = [
        "fiscal", "dívida", "orçamento", "superávit", "teto", "arcabouço",
        "imposto", "reforma tributária", "investimento", "emprego", "energia", "estatais"
    ]
    
    freq_pl, pags_pl = analisar_termos_chave(dados_pl, termos_fiscal)
    freq_pt, pags_pt = analisar_termos_chave(dados_pt, termos_fiscal)
    
    print("\n[+] Amostra de Frequência de Termos-Chave:")
    print(f"{'Termo':<20} | {'PL (Flávio)':<12} | {'PT (Lula)':<12}")
    print("-" * 50)
    for t in termos_fiscal:
        print(f"{t:<20} | {freq_pl[t]:<12} | {freq_pt[t]:<12}")

if __name__ == "__main__":
    main()
