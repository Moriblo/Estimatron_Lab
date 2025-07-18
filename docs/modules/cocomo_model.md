# 🧮 cocomo_model.py

Implementa o cálculo do esforço, prazo e custo do projeto com base no modelo COCOMO II, usando LOC, EAF e salário mensal.

---

## 📦 Funções

### `calcular_cocomo(loc: int, eaf: float, salario_mensal: float) → tuple`
Calcula os valores principais do projeto a partir da fórmula simplificada do modelo COCOMO II.

**Retorna:**
- `esforco`: Pessoa-mês estimado
- `prazo`: Prazo do projeto em meses
- `custo_total`: Valor total em R$

---

## 🔢 Fórmula utilizada

- Esforço = `2.94 * (LOC/1000)^0.91 * EAF`
- Prazo = `3.67 * (Esforço)^0.35`
- Custo = `Esforço * salário_mensal`
