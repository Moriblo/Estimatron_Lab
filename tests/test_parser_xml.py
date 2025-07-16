"""#######################################################################
test_parser_xml.py
📄 Testes unitários — Extração de LOC e blocos de XML UML

Testa a função `extrair_loc_drawio()` com arquivos válidos e inexistentes.
Confere retorno consistente com blocos, LOC e mensagens de erro.

Autor: MOACYR + Copilot
Versão da suíte de testes: 2.2
Data: 2025-07-17
#########################################################################"""

import pytest
from modules.parser_xml import extrair_loc_drawio

# ✅ Arquivo válido retorna LOC positivo e blocos textuais
def test_loc_estimada_xml():
    resultado = extrair_loc_drawio("tests/modelo_xml_curto.xml")
    assert "loc" in resultado
    assert "blocos" in resultado
    assert "erro" in resultado
    assert isinstance(resultado["loc"], int)
    assert resultado["loc"] > 0
    assert isinstance(resultado["blocos"], list)
    assert resultado["loc"] == len(resultado["blocos"])

# ❌ Arquivo inexistente deve retornar erro explícito
def test_arquivo_xml_inexistente():
    resultado = extrair_loc_drawio("tests/nada_existe.xml")
    assert resultado["erro"] is not None
    assert resultado["loc"] == 0
    assert resultado["blocos"] == []


