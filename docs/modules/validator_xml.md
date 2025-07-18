# 🛡️ validator_xml.py

Valida a estrutura de arquivos XML gerados pelo draw.io para garantir que sejam elegíveis para estimativas no Estimatron.

---

## 📦 Funções

### `validar_xml_drawio(xml_path: str) → dict`
Analisa o XML e gera um diagnóstico técnico com insights estruturais e semânticos.

**Retorna:**
- `valido`: True/False baseado na presença de `<mxGraphModel>`
- `tipo_raiz`: Tag raiz do documento
- `xmlns_detectado`: Se o documento possui namespace
- `num_celulas`: Quantidade de `<mxCell>` no arquivo
- `num_blocos_com_texto`: Blocos com valor textual
- `erro`: Erro detectado, se aplicável

---

## 🧪 Critério mínimo

✔️ O documento deve conter `<mxGraphModel>`  
✔️ Deve possuir ao menos 1 bloco com texto (`value`)
