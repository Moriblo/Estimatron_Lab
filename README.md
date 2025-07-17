# 🤖 Estimatron [![Estimatron](https://img.shields.io/badge/Estimatron-Model%20Driven%20Estimator-purple)](https://github.com/moriblo/estimatron)

[![Status](https://img.shields.io/badge/project-active-brightgreen)](https://en.wikipedia.org/wiki/Software_development_process)
[![License](https://img.shields.io/badge/license-MIT-blue)](https://opensource.org/licenses/MIT)
[![Streamlit](https://img.shields.io/badge/built%20with-Streamlit-orange)](https://streamlit.io/)
[![XML Schema](https://img.shields.io/badge/XML%20Schema-W3C%202001-blue.svg?logo=xml&logoColor=white)](http://www.w3.org/2001/XMLSchema)
[![Python](https://img.shields.io/badge/python-3.10%2B-yellow)](https://www.python.org/downloads/release/python-3100/)
[![Cobertura 100%](https://img.shields.io/badge/coverage-100%25-brightgreen)](htmlcov/index.html)

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

---

## 🧮 Significado dos parâmetros COCOMO II

| Parâmetro | Papel no cálculo                | Interpretação prática                                     |
|-----------|---------------------------------|-----------------------------------------------------------|
| `a`       | Constante de produtividade      | Base de esforço por mil linhas de código (KLOC)           |
| `b`       | Expoente de escala              | Representa o crescimento não linear conforme a escala     |
| `c`       | Fator de dimensionamento de prazo | Ajusta o tempo com base no esforço estimado             |

## 📌 Fórmulas envolvidas

- **Esforço (PM):**  
  $$ PM = a \cdot (KLOC)^b \cdot EAF $$

- **Prazo (TDEV):**  
  $$ TDEV = c \cdot (PM)^{0.35} $$

- **Custo total:**  
  $$ Custo = PM \cdot salário\_mensal $$

## 🔢 Valores típicos para projetos padrão

Estes parâmetros são comumente utilizados no modelo COCOMO II:

```text
a = 2.94  # Produtividade base
b = 0.91  # Expoente de escala
c = 3.67  # Fator de prazo (dimensionamento temporal)

Esses valores foram calibrados a partir de estudos sobre centenas de projetos reais e podem ser ajustados conforme o perfil da equipe, domínio técnico ou grau de maturidade.

---

## 💡 O que esperar da interface

### 🔘 Escolha do modo de entrada

- **Manual:** Upload direto dos arquivos XML/XSD + salário mensal
- **Arquivo `config.json`:** Upload de um JSON com os caminhos e valores

---

### 📂 Upload dos arquivos necessários

- `modelo.xml`: exportado do draw.io contendo o diagrama UML
- `modelo.xsd`: representando o esquema estrutural dos dados

---

### 🧪 Diagnóstico técnico automático

Antes da estimativa, o sistema exibe informações dos arquivos analisados:

#### 📄 XML
- Validade estrutural
- Tipo da raiz detectada (`mxGraphModel`, `diagram`, etc.)
- Total de células (`mxCell`)
- Blocos com texto úteis para LOC

#### 📂 XSD
- Quantidade de elementos globais
- Elementos internos e estruturas aninhadas
- Número de `complexTypes`
- Faixa de EAF atribuída com base na complexidade

---

### 📐 Estimativa baseada no modelo COCOMO II

Após clicar em **🚀 Gerar estimativa**, os seguintes dados são calculados e exibidos:

- 🔢 LOC estimado
- ⚙️ Fator de ajuste de complexidade (EAF)
- 🧠 Esforço em pessoa-mês
- 📆 Prazo estimado em meses
- 💸 Custo total do projeto

---

### 📁 Exemplo de arquivo `config.json` para entrada automática

```json
{
  "xml_path": "entradas/modelo.xml",
  "xsd_path": "entradas/modelo.xsd",
  "salario_mensal": 12000
}

> Coloque esse arquivo em `config/config.json` ou selecione via interface.

O **Estimatron** foi projetado para oferecer estimativas **rápidas**, **confiáveis** e **auditáveis**, com validação técnica das entradas antes do processamento.  
Ideal para **analistas de requisitos**, **arquitetos de software** e **engenheiros de estimativas**.

## 🚀 Como executar o Estimatron (`main.py`)

O Estimatron é uma aplicação baseada em Streamlit que realiza estimativas de esforço, prazo e custo de projetos de software utilizando o modelo COCOMO II, com entrada de arquivos UML/XML (draw.io) e XSD.

### ✅ Pré-requisitos

- Python 3.10 ou superior
- Ambiente virtual ativado (`venv`)
- Pacotes instalados via `requirements.txt`
- Arquivos dos módulos e testes no diretório padrão do projeto

### ▶️ Execução

No terminal, dentro da pasta do projeto:

```bash
streamlit run main.py
```

---
---

## 🔄 Novo fluxo automático de entrada (a partir da versão 2.0)

A partir da versão 2.0, o Estimatron foi simplificado para exigir apenas o **upload do arquivo XML**, exportado do draw.io. O sistema agora **gera automaticamente o XSD** com base nos blocos textuais encontrados no modelo UML.

---

### 📂 Entrada única

- `modelo.xml`: diagrama UML exportado em formato XML (draw.io)

> O arquivo `.xsd` é criado internamente pelo sistema — não é necessário fornecê-lo manualmente.

---

### ⚙️ Geração automática do XSD

Após validar a estrutura do XML, o Estimatron:
- Extrai os blocos com texto relevantes (ex: nome de classes, entidades)
- Cria um esquema XSD simples, compatível com padrão XML Schema
- Usa esse arquivo para calcular a **complexidade técnica (EAF)**

---

### 📊 Diagnóstico técnico exibido antes da estimativa

O sistema mostra:

#### 🧪 XML
- Validade da estrutura
- Tipo de raiz detectada
- Número de células (`mxCell`)
- Quantidade de blocos com texto

#### 🧪 XSD (gerado automaticamente)
- Elementos globais e internos
- Número de `complexTypes`
- Total de elementos detectados
- Faixa de EAF atribuída

---

### 📐 Estimativa gerada

Depois de clicar em **🚀 Gerar estimativa**, são exibidos:

- 🔢 LOC estimado
- ⚙️ EAF calculado
- 🧠 Esforço em pessoa-mês
- 📆 Prazo estimado
- 💸 Custo total do projeto

---

Com esse novo fluxo, o Estimatron se torna ainda mais **fácil de usar**, eliminando etapas manuais e proporcionando uma análise técnica automática a partir de uma única entrada XML. Ideal para ambientes ágeis, consultorias, PMOs e times de análise técnica.

