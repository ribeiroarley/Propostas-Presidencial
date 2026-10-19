# Biblioteca de Prompts de Pesquisa, Testes e Checagem Temática (TSE)

Este catálogo reúne prompts modulares e padronizados para interrogar, auditar e testar os planos de governo de Luiz Inácio Lula da Silva (`data/lula.pdf`) e Flávio Bolsonaro (`data/flavio.pdf`) utilizando as bases extraídas em `outputs/extracao_tematica.json` e `outputs/extracao_tematica.md`.

---

## 📌 Sumário
- [1. Perguntas Temáticas Cirúrgicas](#1-perguntas-temáticas-cirúrgicas)
  - [1.1 Saúde](#11-saúde)
  - [1.2 Educação](#12-educação)
  - [1.3 Segurança Pública](#13-segurança-pública)
  - [1.4 Agronegócio & Meio Ambiente](#14-agronegócio--meio-ambiente)
  - [1.5 Economia & Finanças Públicas](#15-economia--finanças-públicas)
- [2. Checagem de Fatos e Viabilidade (Fact-checking & Stress Test)](#2-checagem-de-fatos-e-viabilidade-fact-checking--stress-test)
  - [2.1 Teste de Exigência Legislativa (PEC vs. Lei Ordinária)](#21-teste-de-exigência-legislativa-pec-vs-lei-ordinária)
  - [2.2 Teste de Custo de Oportunidade e Risco Macroeconômico](#22-teste-de-custo-de-oportunidade-e-risco-macroeconômico)
- [3. Prompts para Extração de Citações Literais e Rastreabilidade](#3-prompts-para-extração-de-citações-literais-e-rastreabilidade)

---

## 1. Perguntas Temáticas Cirúrgicas

### 1.1 Saúde
```markdown
# Prompt: Comparação de Modelos na Saúde e Redução de Filas

Contexto: Analise as propostas de Saúde de Lula (páginas 34 a 39) e Flávio (páginas 21-22 e 37-38).
Tarefa: Compare tecnicamente os seguintes pontos:
1. Modelo de Gestão: O plano prioriza a expansão da capacidade própria estatal do SUS ou a contratualização de serviços com a rede privada e filantrópica via PPPs?
2. Fila do SUS: Quais são as metas, prazos e ferramentas operacionais (ex.: telessaúde, mutirões, prontuário digital unificado) para zerar filas de exames especializados e cirurgias eletivas?
3. Complexo Industrial vs. Mercado: Como cada candidato lida com a produção nacional de medicamentos, vacinas e dependência de insumos internacionais?
Formato de Resposta: Tabela comparativa dos 3 pontos seguida por análise de sustentabilidade do custeio.
```

---

### 1.2 Educação
```markdown
# Prompt: Financiamento da Educação Básica e Modelos de Ensino

Contexto: Analise as propostas de Educação de Lula (páginas 30 a 33) e Flávio (páginas 21 e 34 a 36).
Tarefa: Responda de forma objetiva:
1. Financiamento e Alocação: Como os candidatos tratam os recursos públicos? Há incentivo a vouchers privados (ex.: voucher-creche) ou fortalecimento exclusivo da rede pública e do Fundeb?
2. Valorização Docente e Currículo: Quais são as propostas para o Piso Nacional do Magistério, formação continuada e diretrizes curriculares (foco em competências básicas vs. formação integral cidadã)?
3. Ensino Técnico e Profissionalizante: Qual a estratégia para conectar o ensino médio e pós-médio às demandas do mercado de trabalho contemporâneo?
Formato de Resposta: Matriz de convergências, divergências e riscos de implementação de cada abordagem.
```

---

### 1.3 Segurança Pública
```markdown
# Prompt: Doutrina Policial, Inteligência e Crime Organizado

Contexto: Analise as propostas de Segurança Pública de Lula (páginas 26 a 29) e Flávio (páginas 13 a 17).
Tarefa: Avalie tecnicamente:
1. Enfrentamento a Facções Criminosas: O plano privilegia a asfixia financeira e inteligência patrimonial (COAF/PF) ou a neutralização ostensiva e encarceramento em presídios federais de segurança máxima?
2. Armas de Fogo e Legislação Penal: Quais as posições sobre o Estatuto do Desarmamento, porte civil de armas, saidinhas de presos, excludente de ilicitude e Lei Antiterrorismo?
3. Papel das Forças Armadas: Há proposta de emprego constitucional da Marinha, Exército e Aeronáutica no patrulhamento permanente de fronteiras, portos e aeroportos?
Formato de Resposta: Síntese comparativa dos mecanismos de dissuasão criminal propostos.
```

---

### 1.4 Agronegócio & Meio Ambiente
```markdown
# Prompt: Equilíbrio entre Fronteira Produtiva e Metas Climáticas

Contexto: Analise as propostas de Agro e Meio Ambiente de Lula (páginas 20, 58-62 e 69-72) e Flávio (páginas 5, 28, 50, 53-55 e 57-58).
Tarefa: Responda fundamentadamente:
1. Crédito Rural e Sustentabilidade: O crédito agrícola (Plano Safra / financiamento privado) está condicionado a critérios ecológicos ou focado em aumento irrestrito de produtividade?
2. Licenciamento Ambiental e Regularização Fundiária: Qual a posição sobre aprovação tácita de licenças por decurso de prazo, validação do CAR e demarcação de terras indígenas e quilombolas?
3. Ativos Verdes e Mercado de Carbono: Como cada candidato propõe monetizar a matriz ecológica (SAF, biocombustíveis, mercado de carbono regulado)?
Formato de Resposta: Avaliação de risco regulatório e potenciais barreiras comerciais internacionais enfrentadas pelo agronegócio.
```

---

### 1.5 Economia & Finanças Públicas
```markdown
# Prompt: Âncoras Fiscais, Reforma Tributária e Sustentabilidade da Dívida

Contexto: Analise os eixos fiscais e econômicos de Lula (páginas 10-12, 19 e 47-56) e Flávio (páginas 8-9, 12 e 68-72).
Tarefa: Execute uma auditoria fiscal rigorosa:
1. Regime Fiscal: O plano defende o Novo Arcabouço Fiscal (limitação de despesas atrelada a receitas) ou uma nova regra de controle de gastos rígida com corte nominal ("Tesouraço")?
2. Reforma Tributária: Qual a posição sobre o IVA dual da EC nº 132/2023, o Fundo de Desenvolvimento Regional e as exceções setoriais? Há proposta de revisão de alíquotas ou desoneração de investimentos?
3. Equação de Custeio: Quais despesas são prometidas e quais receitas permanentes ou cortes de despesas obrigatórias são expressamente apontados como contrapartida?
Formato de Resposta: Tabela de receitas vs. despesas projetadas e balanço da trajetória da relação Dívida/PIB.
```

---

## 2. Checagem de Fatos e Viabilidade (Fact-checking & Stress Test)

### 2.1 Teste de Exigência Legislativa (PEC vs. Lei Ordinária)
```markdown
# Prompt de Fact-checking: Risco Legislativo e Quórum Parlamentar

Papel: Consultor Legislativo e Auditor Constitucional.
Entrada: [Insira a promessa específica do candidato extraída do plano de governo].
Tarefa:
1. Identifique a natureza jurídica da proposta: ela pode ser implementada por Decreto/Portaria (poder regulamentar do Executivo), Lei Ordinária (maioria simples no Congresso), Lei Complementar (maioria absoluta) ou exige Proposta de Emenda à Constituição - PEC (quórum de 3/5 em dois turnos na Câmara e no Senado)?
2. Avalie a viabilidade política: considerando a correlação de forças tradicional do Congresso brasileiro, qual é o grau de resistência corporativa, federativa ou partidária à medida?
3. Veredito de Exequibilidade: Classifique como Alta, Média ou Baixa viabilidade legislativa e justifique.
```

---

### 2.2 Teste de Custo de Oportunidade e Risco Macroeconômico
```markdown
# Prompt de Stress Test: Custo de Oportunidade e Choque Macroeconômico

Papel: Econometrista e Analista de Cenários Macroeconômicos.
Entrada: [Insira a política econômica ou fiscal pretendida].
Tarefa:
1. Canal de Transmissão da Inflação e Juros: Essa política pressiona a demanda agregada no curto prazo gerando pressão inflacionária e elevação da Selic, ou promove choque de oferta deflacionário?
2. Impacto na Dívida Pública: Qual o efeito líquido estimado sobre o déficit primário e sobre o custo médio de rolagem da Dívida Bruta do Governo Geral (DBGG)?
3. Efeito Alocativo: A medida gera crowding-in (atração de investimento privado) ou crowding-out (expulsão de capital privado por absorção estatal de poupança)?
Formato de Resposta: Relatório de risco com três cenários: Base, Otimista e Estresse.
```

---

## 3. Prompts para Extração de Citações Literais e Rastreabilidade

```markdown
# Prompt de Rastreamento Documental Estrito (Evidência Factual)

Papel: Auditor de Conformidade e Verificação Documental.
Pergunta: "Qual é a posição exata do candidato [Lula / Flávio] sobre [Tema/Termo-chave: ex. escala 6x1, Lei das Estatais, voucher-creche, imposto sobre super-ricos]?"
Instruções Obrigatórias:
1. Recupere o número exato da página no arquivo original (`data/lula.pdf` ou `data/flavio.pdf`).
2. Transcreva o trecho literal entre aspas duplas, sem paráfrases ou interpretações intermediárias.
3. Indique o contexto do capítulo ou seção em que a passagem está inserida.
4. Caso o documento seja silente ou omisso a respeito do termo pesquisado, declare explicitamente: "Omissão Documental: Nenhuma menção direta ou indireta localizada no plano protocolado no TSE."
```
