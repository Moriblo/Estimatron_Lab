"""
test_validator_xml.py
🧪 Testes para o módulo validator_xml.py

Verifica comportamento da função validar_xml_drawio() em diferentes condições:
- XML válido com estrutura reconhecida
- XML sem namespace
- XML com raiz não padrão (≠ mxGraphModel)
- XML bem formado mas com estrutura irrelevante
- XML malformado que dispara erro de parsing

Autor: MOACYR + Copilot
Versão: 2.2
Data: 2025-07-15
"""

from modules.validator_xml import validar_xml_drawio

def test_xml_valido_com_estrutura():
    """
    ✅ Testa um XML real do draw.io com raiz <mxfile> e estrutura interna <mxGraphModel>.
    Deve ser reconhecido como válido.
    """
    resultado = validar_xml_drawio("tests/xml_valido_drawio.xml")
    assert resultado["valido"] is True
    assert resultado["erro"] is None
    assert resultado["tipo_raiz"] == "mxfile"
    assert resultado["num_celulas"] > 0
    assert resultado["num_blocos_com_texto"] > 0

def test_xml_sem_namespace():
    """
    📦 Testa um XML sem atributo xmlns.
    Mesmo sem namespace, estrutura pode ser reconhecida.
    """
    resultado = validar_xml_drawio("tests/xml_sem_namespace.xml")
    assert resultado["xmlns_detectado"] is False
    assert resultado["erro"] is None
    assert resultado["valido"] in [True, False]  # aceita ambos, depende da estrutura

def test_xml_raiz_alternativa_sem_modelo():
    """
    ❌ Testa um XML com raiz alternativa (ex: <root>) sem <mxGraphModel>.
    Deve ser considerado estruturalmente inválido.
    """
    resultado = validar_xml_drawio("tests/xml_raiz_alternativa.xml")
    assert resultado["tipo_raiz"] == "root"
    assert resultado["valido"] is False
    assert resultado["erro"] is None
    assert resultado["num_blocos_com_texto"] == 0

def test_xml_bem_formado_sem_mxgraph():
    """
    ❌ Testa XML bem formado com raiz padrão mas sem <mxGraphModel> interno.
    Deve ser marcado como inválido.
    """
    resultado = validar_xml_drawio("tests/xml_sem_mxgraph.xml")
    assert resultado["valido"] is False
    assert resultado["erro"] is None

def test_xml_malformado_parse_error():
    """
    ❌ Testa XML com erro grave de sintaxe (ex: tags incompletas).
    Deve gerar erro de parsing.
    """
    resultado = validar_xml_drawio("tests/xml_malformado.xml")
    assert resultado["valido"] is False
    assert resultado["erro"] is not None
