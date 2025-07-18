
---

### 📄 `parser_xsd.md`

```markdown
# 📂 parser_xsd.py

Funções que analisam o arquivo XSD gerado e calculam o EAF (Effort Adjustment Factor) com base na estrutura e complexidade do schema.

---

## 📦 Funções

### `calcular_eaf_xsd(xsd_path: str) → dict`
Verifica a presença de elementos globais, internos e complexTypes em um esquema XSD. Utiliza isso para estimar a complexidade técnica.

**Retorna:**
- `elementos_globais`: Total de elementos independentes
- `elementos_internos`: Elementos dentro de tipos complexos
- `complex_types`: Quantidade de `<xs:complexType>`
- `total_elementos`: Soma total dos componentes
- `eaf`: Fator de ajuste calculado (0.85, 1.00 ou 1.15)
- `erro`: Mensagem de erro, se aplicável

---

## 📊 Faixa EAF

| Total de elementos | Complexidade | EAF |
|--------------------|--------------|-----|
| 0–4                | Baixa        | 0.85 |
| 5–15               | Média        | 1.00 |
| >15                | Alta         | 1.15 |
