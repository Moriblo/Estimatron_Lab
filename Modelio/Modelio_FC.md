# 📘 Estrutura do Guia: Pontos de Função via Modelio

## 🧭 Etapas do Fluxo e Suas Zonas de Contagem

| 🔹 Etapa Institucional | 📐 Elementos Modelados          | 🧩 PF Mapeável | 🔎 Observações                                           |
|------------------------|-------------------------------|----------------|---------------------------------------------------------|
| VisaoDoSistema         | Activity, Process BPMN        | EE / CE        | Tarefas podem ser contadas como funcionalidades         |
| IdStakeholders         | Classe Template_Stakeholder   | --             | Não gera PF direto, mas mapeia atores                  |
| LevReqFunc             | UseCases, Actors              | EE / CE / SE   | Associado a entradas, consultas e saídas               |
| LevReqNFunc            | Classe Template_RNF           | --             | Requisitos qualificam, mas não geram PF direto         |
| ModUCTec               | Classes com `<<Entidade>>`    | AR / ALI       | Contam como funções de dados internas/externas         |
| MapRN                  | Classes `<<RegraNegocio>>`    | --             | Influenciam contagem de complexidade                   |
| AtualGTec              | Template_GL000                | --             | Sem contagem direta, auxilia consistência              |
| ConsRelpRast           | Template_TR                   | --             | Mapeia vínculos para auditoria e consistência          |

---

## 🛠 Elementos UML e Suas Equivalências para PF

| 🧩 Elemento UML              | 📏 Tipo PF (IFPUG) | 💡 Estereótipo / Regra de Extração              |
|-----------------------------|-------------------|-------------------------------------------------|
| `UseCase`                   | EE / SE / CE      | Base no propósito e relacionamento com ator     |
| `Class <<Entidade>>`        | AR                | Interna, manipulada pelo sistema                |
| `Class <<EntidadeExterna>>` | ALI               | Externa, apenas lida no sistema                 |
| `Actor`                     | --                | Fonte de dados, não conta direto                |
| `Association`               | --                | Indica complexidade ou interdependência         |
| `Activity` técnica          | --                | Local onde os elementos são agrupados           |
| `Note` orientativa          | --                | Documenta tipo PF, critério e justificativa     |

---

## 📂 Exemplo Prático de Modelagem Contável

### 🔹 Etapa: LevReqFunc

```plaintext
Activity: UseCases_Activity
├─ UseCase: UC001_SolicitarAtendimento (Tipo: EE)
│   └─ Actor: Cliente
│   └─ Classe relacionada: Cliente (<<Entidade>> → AR)
│   └─ RNF relacionada: RNF001_TempoDeResposta
│   └─ Regra: RN001_TarifaEspecial
├─ UseCase: UC002_VisualizarAtendimentos (Tipo: CE)
│   └─ Actor: Cliente
│   └─ Classe relacionada: Atendimento (<<Entidade>> → AR)

🔎 Cada linha acima pode ser exportada via XMI e lida por um parser automatizado para geração de relatório PF.
```
---

## ✨ Orientações Adicionais para o Analista

Toda UseCase deve conter:

Nome claro

Estereótipo indicando tipo PF (<<Entrada>>, <<Consulta>>)

Atores primários associados

Classes envolvidas (AR / ALI)

Os templates orientadores (como Template_UC000) devem conter campos:

Tipo PF

Complexidade esperada

Justificativa e critérios

## 📊 Proposta de Automação Futuro
Você poderá criar ou conectar uma ferramenta que:

Leia o XMI exportado pelo Modelio

Identifique os elementos modelados com estereótipos específicos

Classifique os itens conforme regras de contagem PF

Gere relatório .CSV ou .XLS com estimativa total de FC

Inclua links reversos para auditoria e rastreamento
