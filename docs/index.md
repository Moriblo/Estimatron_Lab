# 🏠 Estimatron

**Estimativas inteligentes de esforço e cronograma** com base em diagramas UML extraídos via draw.io.

---

## 🚀 O que é?

O Estimatron é uma ferramenta leve e técnica que interpreta diagramas XML exportados do draw.io e aplica modelos de análise como Function Points e COCOMO II para gerar estimativas realistas de desenvolvimento — incluindo esforço, prazo e custo.

---

## 🔍 Principais funcionalidades

- Validação estrutural de arquivos XML UML
- Geração automática de schemas XSD
- Cálculo do fator de complexidade (EAF)
- Aplicação do modelo COCOMO II
- Interface interativa via Streamlit
- Documentação técnica via MkDocs

---

## 📦 Módulos

Consulte a seção [Módulos](./modules/parser_xml.md) para conhecer a estrutura técnica do sistema.

---

## 🧭 Como iniciar

```bash
pip install -r requirements.txt
streamlit run main.py
