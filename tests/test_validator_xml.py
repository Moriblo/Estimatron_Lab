"""###############################################################################
test_validator_xml.py
🔍 Testes unitários — Validação estrutural de XML UML

Testa a função `validar_xml_drawio()` para XMLs válidos, malformados e sem blocos.
Verifica tipo de raiz, namespace e contagem de elementos.

Autor: MOACYR + Copilot
Versão da suíte de testes: 2.2
Data: 2025-07-17
##################################################################################"""

from modules.validator_xml import validar_xml_drawio

# ✅ XML válido com blocos
def test_xml_valido():
    resultado = validar_xml_drawio("tests/xml_exemplo_valido.xml")
    assert resultado["valido"] is True
    assert resultado["erro"] is None
    assert resultado["num_blocos_com_texto"] > 0

# ❌ XML malformado
def test_xml_malformado():
    resultado = validar_xml_drawio("tests/xml_malformado.xml")
    assert resultado["valido"] is False
    assert resultado["erro"] is not None

# ❌ XML vazio
def test_xml_vazio():
    resultado = validar_xml_drawio("tests/xml_vazio.xml")
    assert resultado["valido"] is False
    assert resultado["erro"] is not None

# ✅ XML sem blocos com texto
def test_xml_sem_blocos():
    resultado = validar_xml_drawio("tests/xml_sem_blocos.xml")
    assert resultado["valido"] is True
    assert resultado["num_blocos_com_texto"] == 0

# ✅ XML sem namespace
def test_xml_sem_namespace():
    resultado = validar_xml_drawio("tests/xml_sem_namespace.xml")
    assert resultado["valido"] is False  # depende do que o validador considera válido
    assert resultado["tipo_raiz"] == "root"

# ❌ XML raiz não padrão
def test_xml_raiz_nao_padrao():
    resultado = validar_xml_drawio("tests/xml_raiz_alternativa.xml")
    assert resultado["tipo_raiz"] == "root"  # ou o nome da tag que você usar
    assert resultado["valido"] is False
    assert resultado["erro"] is None
    assert resultado["num_blocos_com_texto"] == 0
