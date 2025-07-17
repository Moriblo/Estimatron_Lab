# 🔧 Pipeline Proposto: Visão Geral

Você quer partir de um arquivo UML (Draw.io) e gerar uma análise completa com:

- 📊 **Estimativas LOC e Function Points** a partir da estrutura do sistema.
- 🧠 **Cálculo com base no COCOMO II**, detalhando:
  - Percentual de esforço por perfil profissional (com níveis de expertise).
  - Distribuição por disciplinas x fases.
- ⚙️ **Consideração de parâmetros ajustáveis**: tamanho do projeto, maturidade da equipe, automação, etc.

---

## 🗂️ Etapas do Pipeline

### 1. Entrada UML (Draw.io) → XML/XSD
- Ferramentas: Draw.io exporta diretamente para XML.
- A partir do XML/XSD, podemos extrair:
  - Classes, atributos, relacionamentos.
  - Tipos de componentes que mapeiam para Function Points.

### 2. Parser XML/XSD → Categorização FP
- Criar um parser que identifique os 5 componentes de FP:
  - **EE**, **SE**, **CE**, **ALI**, **AIE**
- Regras heurísticas (ex: métodos que manipulam dados externos = EE)

### 3. LOC Estimation
- Baseado em número de classes, métodos e complexidade estimada.
- Ferramentas possíveis: *Lizard*, *SLOCCount* (adaptados para UML)

### 4. Cálculo Function Points
- Regras de contagem por **IFPUG** (pesos por tipo e complexidade)
- Resultado: valor total de **FP**

---

## 📐 COCOMO II – Estimativa de Esforço e Cronograma

### Parâmetros e Impacto

| Parâmetro                    | Variáveis possíveis          | Impacto no modelo                                 |
|-----------------------------|------------------------------|---------------------------------------------------|
| Tamanho do projeto          | Pequeno, Médio, Grande       | Afeta multiplicadores de esforço e tempo          |
| Maturidade da equipe        | Alta, Média, Baixa           | Ajusta fator de produtividade                     |
| Ferramentas de automação    | Nenhuma, Parcial, Total      | Reduz esforço em certas disciplinas               |
| Automação testes/deployment | Nenhuma, Parcial, Total      | Reduz tempo de teste e implantação                |

---

## 👥 Distribuição por Skills e Expertise

| Skill               | Jr.  | Pl.  | Sr.  | Observações                             |
|---------------------|------|------|------|-----------------------------------------|
| BA (Business Analyst)| 10%  | 15%  | 5%   | Mais presente nas fases iniciais        |
| Dev (Desenvolvedor) | 25%  | 20%  | 15%  | Construção e testes                     |
| Eng./Cientista de BD| 10%  | 10%  | 5%   | Análise/design, implantação             |
| Testers             | 10%  | 10%  | 5%   | Fase de testes e transição              |

> *Esses valores podem ser ajustados com base em métricas históricas do time.*

---

## 📆 Distribuição por Fase e Disciplina

| Disciplina              | Concepção | Elaboração | Construção | Transição |
|-------------------------|-----------|------------|------------|-----------|
| Modelagem de Negócios   | 40%       | 20%        | 0%         | 0%        |
| Requisitos              | 30%       | 30%        | 10%        | 0%        |
| Gerenciamento de Projeto| 10%       | 20%        | 20%        | 10%       |
| Ambiente                | 5%        | 10%        | 10%        | 5%        |
| Configuração            | 0%        | 10%        | 10%        | 10%       |
| Análise e Design        | 15%       | 30%        | 10%        | 0%        |
| Testes                  | 0%        | 10%        | 20%        | 30%       |
| Implementação           | 0%        | 5%         | 20%        | 20%       |
| Implantação             | 0%        | 0%         | 0%         | 25%       |

> *Esses números podem ser gerados com base em fórmulas do COCOMO II e ajustados por fatores de projeto.*

---

## 🧠 Próximos Passos

Posso te ajudar a começar esse pipeline com:

- 🔧 Roteiro de arquitetura técnica (linguagens, libs, ferramentas)
- 🧪 Esboço de scripts iniciais para parser Draw.io → FP
- 📐 Modelo ajustado para aplicar COCOMO II com base nos parâmetros

---

Curtiu a estrutura? Posso adaptar ou expandir algum trecho, se quiser. Vamos colocar isso em produção? 🚀
