# 📦 Estimatron — Histórico de alterações técnicas

Projeto: Estimatron (estimativa COCOMO II via XML/XSD)
Autor: MOACYR + Copilot  
Formato: Markdown  
Última revisão: 2025-07-16  

---

## ✅ Versão 2.1 — [2025-07-16]

### 🚀 Refatorações principais
- **Remoção total da dependência do `config.json`**
  - Todos os caminhos de arquivos agora são passados via parâmetros
  - Módulos `parser_xml`, `parser_xsd`, `validator_xml`, `main.py` revisados
  - Mensagens de erro no navegador eliminadas

- **Padronização de argumentos**
  - Uso consistente de `xml_path`, `xsd_path` nos módulos
  - Interface mais intuitiva e segura para chamadas internas

### 🧼 Organização de arquivos
- **Função `limpar_arquivos_temp()` adicionada**
  - Remove `temp_modelo.xml` e `temp_modelo.xsd` automaticamente após estimativa
  - Versão robusta com `try...except` e tratamento de falhas

### 🔧 Automação via terminal
- **Scripts `.bat` criados e comentados**
  - `estimatron.bat`: ativa o venv e roda o Streamlit
  - `estimatron-dev.bat`: ativa o venv e roda testes com cobertura

- **Tarefas no VS Code (`tasks.json`)**
  - `🚀 Iniciar Estimatron` e `🧪 Rodar testes` disponíveis como tarefas nativas
  - Atalhos de teclado personalizados via `keybindings.json`

### 🧠 Validação técnica
- **Função `validar_xml_drawio()` atualizada**
  - Versão 1.2 oficializada com captura de raiz, namespace, blocos com texto
  - Retorno expandido e padronizado

---

## 📦 Versão 2.0 — [2025-07-15]

- Implementação da geração automática de XSD com base nos blocos detectados
- Introdução do módulo `parser_xsd.py` para cálculo de EAF técnico
- Integração completa com estimativa COCOMO II no `main.py`

---

## 📦 Versão 1.0 — [2025-07-14]

- Protótipo inicial com upload de XML e cálculo básico de LOC
- Geração manual do XSD
- Interface com Streamlit em fase experimental

---

> Para evoluções futuras, considera-se incluir:
> - Logs com timestamp
> - Exportação de relatórios de estimativa
> - Suporte a múltiplos arquivos ou modelos concorrentes

