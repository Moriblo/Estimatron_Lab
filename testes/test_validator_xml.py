"""
🧪 Testes para o módulo validator_xml.py

Verifica a robustez da validação estrutural de arquivos XML exportados do draw.io,
incluindo casos válidos, malformados, sem blocos com texto e variações de estrutura.

Autor: MOACYR + Copilot
Versão: 1.1
Data: 2025-07-15
"""

import pytest
from modules.validator_xml import validar_xml_drawio

def test_xml_valido():
    resultado = validar_xml_drawio("testes/xml_exemplo_valido.xml")
    exibir_diagnostico(resultado)
    assert resultado["valido"]
    assert "mxGraphModel" in resultado["tipo_raiz"]
    assert resultado["num_blocos_com_texto"] > 0

def test_xml_malformado():
    resultado = validar_xml_drawio("testes/xml_malformado.xml")
    exibir_diagnostico(resultado)
    assert not resultado["valido"]
    assert "XML mal formado" in resultado["erro"] or "Falha inesperada" in resultado["erro"]

def test_xml_vazio():
    resultado = validar_xml_drawio("testes/xml_vazio.xml")
    exibir_diagnostico(resultado)
    assert not resultado["valido"]
    assert resultado["erro"] is not None

def test_xml_sem_blocos():
    resultado = validar_xml_drawio("testes/xml_sem_blocos.xml")
    exibir_diagnostico(resultado)
    assert resultado["valido"]
    assert resultado["num_blocos_com_texto"] == 0

def exibir_diagnostico(resultado):
    print(f"\n📁 Arquivo analisado: {resultado['arquivo']}")
    print(f"✅ Validade estrutural: {'Válido' if resultado['valido'] else 'Inválido'}")
    print(f"🔖 Tipo de raiz: {resultado.get('tipo_raiz', 'Indefinida')}")
    print(f"🔢 Células totais: {resultado['num_celulas']}")
    print(f"📝 Blocos com texto: {resultado['num_blocos_com_texto']}")
    if resultado["erro"]:
        print(f"❌ Erro detectado: {resultado['erro']}")
