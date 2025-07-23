# 🧭 Etapa: VisaoDoSistema

## 📘 Finalidade

Esta etapa representa o levantamento, registro e validação da visão geral do sistema, incluindo escopo, fronteiras, funcionalidades principais e contexto de origem. Serve como ponto de partida para o entendimento do projeto e alinhamento com o cliente.

---

## 📦 Elementos do Template

### 🔹 1. Activity: `VisaoDoSistema_Activity`

#### Fluxo interno no Activity Diagram:

```plaintext
[Initial Node]
   ↓
Action: Definir Escopo do Sistema
   ↓
Decision: Possui sistemas legados?
   ├─ Sim → Action: Mapear Interfaces Externas
   └─ Não → Action: Identificar funcionalidades principais
   ↓
Action: Validar fronteiras do sistema
   ↓
[Final Node]
```
---
### 🔹 Locals sugeridos

| Nome                | Tipo   | Finalidade                                    |
|---------------------|--------|-----------------------------------------------|
| `SistemaOrigem`     | String | Nome do sistema anterior (se existir)         |
| `FuncionalidadeChave` | Lista  | Funcionalidades centrais identificadas        |
| `InterfaceExterna` | Lista  | Interfaces com sistemas terceiros             |
---
### 🔹 2. Classe Template: `Template_ContextoProjeto`

```text
ID_Item: VG001  
Cliente: [Nome da organização solicitante]  
Descrição: Breve explicação do escopo e objetivo do projeto  
ProblemaAtacado: [O que se busca resolver]  
SoluçãoProposta: [Resumo da solução]  
StakeholdersPrincipais: [Lista dos interessados chave]  
VersãoDocumento: 1.0  
OrigemProjeto: [Nome do sistema ou demanda]
---
### 🔹 3. Processo BPMN: `VisaoDoSistema_BPMN_Process`

| Elemento BPMN                | Tipo         | Propósito                                         |
|-----------------------------|--------------|---------------------------------------------------|
| Pool: Cliente               | Pool         | Parte interessada que fornece requisitos iniciais |
| Pool: Analista              | Pool         | Responsável pela modelagem da visão               |
| Task: Enviar briefing inicial | Task       | Início da coleta de informações                   |
| Task: Registrar contexto    | Task         | Registro de informações no template               |
| Task: Validar escopo        | Task         | Reunião para alinhamento final da visão           |
| Message Flow                | Comunicação  | Troca de dados entre Cliente e Analista           |
| End Event: Visão Definida   | Evento Final | Encerramento da etapa                             |
---
## 📝 Orientações para o Analista

- Não é necessário adicionar novos elementos: **apenas preencher os existentes**
- Utilize o campo `Description` da classe `Template_ContextoProjeto` para **descrever o escopo do sistema**
- Complete o diagrama **BPMN** com os dados obtidos no **briefing inicial**
- Mantenha **rastreabilidade** entre o fluxo institucional e a `Activity VisaoDoSistema_Activity`
- A documentação final pode servir como **insumo para as próximas etapas**:
  - Levantamento de Requisitos
  - Definição de Casos de Uso
  - Modelagem Técnica

