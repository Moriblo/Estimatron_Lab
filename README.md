# 🤖 Estimatron [![Estimatron](https://img.shields.io/badge/Estimatron-Model%20Driven%20Estimator-purple)](https://github.com/moriblo/estimatron)

[![Status](https://img.shields.io/badge/project-active-brightgreen)](https://en.wikipedia.org/wiki/Software_development_process)
[![License](https://img.shields.io/badge/license-MIT-blue)](https://opensource.org/licenses/MIT)
[![Streamlit](https://img.shields.io/badge/built%20with-Streamlit-orange)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/python-3.10%2B-yellow)](https://www.python.org/downloads/release/python-3100/)

> Estimatron é uma ferramenta inteligente para estimativas de esforço, tempo e custo em projetos de software, baseada em modelagem UML e arquivos técnicos XML/XSD, com aplicação automática do modelo COCOMO II.

---

## 📘 Visão Geral

O **Estimatron** é uma PoC que automatiza estimativas de esforço, prazo e custo de software com base em artefatos técnicos como modelos UML (XML do Draw.io) e esquemas XSD. Ele utiliza COCOMO II para gerar projeções realistas, com visualização simplificada e amigável.

Ele integra:

- ✏️ Análise de diagramas UML exportados como XML
- 📂 Interpretação técnica de arquivos XSD
- ⚙️ Cálculo de LOC e EAF
- 📊 Aplicação do modelo COCOMO II
- 🖼️ Interface visual com Streamlit
- 📄 Relatórios simples de estimativa

---

## 🗂️ Estrutura de Diretórios

```text
🤖 estimatron/
├── 🎛️ main.py             # Interface Streamlit com entrada manual ou via config.json
├── ⚙️ config.json         # Parâmetros de entrada opcional
├── 📂 arquivos/           # Diretório dos arquivos de entrada
│   ├── 📄 modelo_uml.xml
│   └── 📄 modelo.xsd
├── 🧩 modules/            # Módulos funcionais do sistema
│   ├── 🧮 parser_xml.py   # Analisa UML/Draw.io (XML) e calcula LOC
│   ├── 📐 parser_xsd.py   # Analisa XSD e gera fator de ajuste (EAF)
│   └── 🧠 cocomo_model.py # Aplica o modelo COCOMO II
```
---

## 🛠️ Como Executar

### 1. Clone o projeto

```bash
git clone https://github.com/seu-usuario/estimatron.git
cd estimatron


