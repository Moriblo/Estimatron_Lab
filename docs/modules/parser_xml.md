# 📄 parser_xml.py

Funções responsáveis pela extração de blocos textuais e cálculo de LOC (Lines of Code) a partir de modelos UML exportados via draw.io.

---

## 📦 Funções

### `extrair_loc_drawio(xml_path: str) → dict`
Analisa um arquivo XML e retorna os blocos que contêm texto. Cada bloco é considerado um candidato a contagem de LOC.

**Parâmetros:**
- `xml_path`: Caminho para o arquivo XML a ser analisado

**Retorna:**
- `loc`: Total de blocos detectados
- `blocos`: Lista de valores textuais
- `erro`: Mensagem de erro, se houver

---

## 🧪 Exemplo de uso

```python
resultado = extrair_loc_drawio("modelo.xml")
print(resultado["loc"])  # → 17
print(resultado["blocos"])  # → ["Login", "Validação", ...]
