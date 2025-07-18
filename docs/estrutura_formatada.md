
---

### 🧩 `estrutura_formatada.md`

```markdown
# 📦 Estrutura Técnica do Estimatron

O projeto segue uma arquitetura modular, organizada em camadas lógicas que se comunicam por meio de chamadas diretas. Abaixo, uma visão tabular dos principais componentes:

---

## 🗂️ Tabela de Módulos Funcionais

| 📁 Módulo               | 🧩 Função Principal                      | 🔍 Propósito                                                                 |
|------------------------|------------------------------------------|------------------------------------------------------------------------------|
| `main.py`              | `gerar_xsd_basico`, `limpar_arquivos_temp` | Interface via Streamlit e coordenação da estimativa                        |
| `parser_xml.py`        | `extrair_loc_drawio`                     | Extração de LOC e blocos textuais via XML do draw.io                       |
| `parser_xsd.py`        | `calcular_eaf_xsd`                       | Estimativa de complexidade e EAF via schema XML                            |
| `validator_xml.py`     | `validar_xml_drawio`                     | Diagnóstico técnico do XML UML                                              |
| `cocomo_model.py`      | `calcular_cocomo`                        | Cálculo de esforço, prazo e custo via modelo COCOMO II                     |

---

## 📐 Fluxo Simplificado

```mermaid
graph TD
    A[Upload XML] --> B[Validar XML]
    B --> C[Extrair LOC]
    C --> D[Gerar XSD]
    D --> E[Calcular EAF]
    E --> F[Executar COCOMO II]
    F --> G[Exibir Estimativa]
