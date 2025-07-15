# 🤖 Estimatron

> Estimatron é uma ferramenta inteligente para estimativas de esforço, tempo e custo em projetos de software, baseada em modelagem UML e arquivos técnicos XML/XSD, com aplicação automática do modelo COCOMO II.

---

## 📘 Visão Geral

O **Estimatron** nasceu como uma PoC (Prova de Conceito) para demonstrar como é possível automatizar estimativas de projetos de software com base em artefatos técnicos gerados desde a modelagem inicial (UML no Draw.io) até os esquemas de dados (XSD).

Ele integra:

- ✏️ Análise de diagramas UML exportados como XML
- 📂 Interpretação técnica de arquivos XSD
- ⚙️ Cálculo de LOC e EAF
- 📊 Aplicação do modelo COCOMO II
- 🖼️ Interface visual com Streamlit
- 📄 Relatórios simples de estimativa

---

## 🗂️ Estrutura do Projeto

estimatron/
|
├── main.py # Interface Streamlit com entrada manual ou via config.json 
|
├── config.json # Parâmetros de entrada opcional
|
├── arquivos/ # Diretório dos arquivos de entrada 
│ ├── modelo_uml.xml 
│ └── modelo.xsd
|
├── modules/ # Módulos funcionais do sistema 
│ ├── parser_xml.py # Analisa UML/Draw.io (XML) e calcula LOC 
│ ├── parser_xsd.py # Analisa XSD e gera fator de ajuste (EAF) 
│ └── cocomo_model.py # Aplica o modelo COCOMO II

