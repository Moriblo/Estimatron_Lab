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
├── 🎛️ main.py               # Interface Streamlit com entrada manual ou via config.json
├── ⚙️ config.json           # Parâmetros de entrada opcional
├── 📦 requirements.txt      # Dependências principais para rodar o Estimatron
├── 🧪 requirements-dev.txt  # Dependências extras para testes e qualidade de código
├── 📂 arquivos/             # Diretório dos arquivos de entrada reais
│   ├── 📄 modelo_uml.xml           # Modelo UML exportado do Draw.io
│   └── 📄 modelo.xsd               # Schema técnico para estimativa de EAF
├── 🧩 modules/              # Módulos funcionais do sistema
│   ├── 🧮 parser_xml.py           # Analisa UML/Draw.io (XML) e calcula LOC
│   ├── 📐 parser_xsd.py           # Analisa XSD e gera fator de ajuste (EAF)
│   └── 🧠 cocomo_model.py         # Aplica o modelo COCOMO II
├── 🧪 testes/               # Testes unitários com dados sintéticos
│   ├── 🧾 modelo_xml_curto.xml      # Modelo UML simplificado para teste de LOC
│   ├── 🧾 xsd_simples.xsd           # Schema com baixa complexidade (<10)
│   ├── 🧾 xsd_medio.xsd             # Schema com complexidade moderada (10–30)
│   ├── 🧾 xsd_intermediario.xsd     # Schema com complexidade técnica (30–60)
│   ├── 🧾 xsd_complexo.xsd          # Schema com alta complexidade (>60)
│   ├── ⚗️ test_parser_xml.py        # Testes para LOC baseado em XML/UML
│   ├── ⚗️ test_parser_xsd.py        # Testes para cálculo de EAF baseado em XSD
│   └── ⚗️ test_cocomo.py            # Testes para estimativa de esforço/prazo/custo
```
---

## 📦 Instalação de dependências

O projeto Estimatron utiliza dois arquivos principais para organizar suas bibliotecas:

- `requirements.txt` → **Dependências essenciais** para rodar o aplicativo via Streamlit
- `requirements-dev.txt` → **Ferramentas adicionais** para testes automatizados e análise de qualidade

Para instalar as dependências básicas, execute:

```bash
pip install -r requirements.txt
```
Se for contribuir com testes ou desenvolvimento interno, instale também:

```bash
pip install -r requirements-dev.txt
```
> 💡 **Dica:** Se estiver usando ambiente virtual (recomendado), ative antes de instalar:
```bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows
```

## 🛠️ Como Executar

### 1. Clone o projeto

```bash
git clone https://github.com/seu-usuario/estimatron.git
cd estimatron
```
### 2. Instale as dependências do projeto

```bash
pip install streamlit xmlschema
```
### 3. Execute o aplicativo via Streamlit

```bash
streamlit run main.py
```
### ✅ O que esperar na execução

- 👤 Escolher o modo de entrada: manual ou via `config.json`
- 📂 Carregar os arquivos necessários (`modelo_uml.xml`, `modelo.xsd`)
- 📊 Visualizar estimativas de:
  - 📏 LOC (Linhas de Código)
  - ⚙️ EAF (Fator de Ajuste Técnico)
  - 🧠 Esforço em pessoa-mês
  - 📆 Prazo do projeto
  - 💰 Custo total com base no salário informado



