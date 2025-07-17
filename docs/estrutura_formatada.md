## 📁 Estrutura de Pastas do Projeto Estimatron

├── 📄 CHANGELOG.md # Log de Features e Releases
├── 📄 README.md
├── 📄 README_Inicial.md
├── 📚 docs/ # Documentação técnica e estrutura gerada
│   └── 📄 estrutura_formatada.md
├── ⚗️ estimatron_gera_estrutarvore.py # Geração da estrutura de pastas
├── ⚗️ main.py # Interface Streamlit com entrada manual ou via config.json
├── 🧠 modules/ # Módulos funcionais do sistema
│   ├── ⚗️ __init__.py
│   ├── 📁 __pycache__/
│   ├── ⚗️ cocomo_model.py
│   ├── ⚗️ parser_xml.py
│   ├── ⚗️ parser_xsd.py
│   └── ⚗️ validator_xml.py
├── 📄 pytest.ini
├── 📄 requirements-dev.txt # Ferramentas extras para testes e qualidade de código
├── 📄 requirements.txt # Dependências principais para rodar o Estimatron
├── ⚗️ setup.py
├── 🧪 tests/ # Testes unitários com dados sintéticos
│   ├── ⚗️ __init__.py
│   ├── 📁 __pycache__/
│   ├── 🧾 modelo_xml_curto.xml # Modelo UML simplificado para teste de LOC
│   ├── ⚗️ test_cocomo.py
│   ├── ⚗️ test_parser_xml.py
│   ├── ⚗️ test_parser_xsd.py
│   ├── ⚗️ test_validator_xml.py
│   ├── 🧾 xml_exemplo_valido.xml
│   ├── 🧾 xml_malformado.xml
│   ├── 🧾 xml_raiz_alternativa.xml
│   ├── 🧾 xml_sem_blocos.xml
│   ├── 🧾 xml_sem_mxgraph.xml
│   ├── 🧾 xml_sem_namespace.xml
│   ├── 🧾 xml_valido_drawio.xml
│   ├── 🧾 xml_vazio.xml
│   ├── 🧾 xsd_complexo.xsd
│   ├── 🧾 xsd_intermediario.xsd
│   ├── 🧾 xsd_malformado.xsd
│   ├── 🧾 xsd_malformado_fatal.xsd
│   ├── 🧾 xsd_medio.xsd
│   └── 🧾 xsd_simples.xsd # Schema com baixa complexidade (<10)