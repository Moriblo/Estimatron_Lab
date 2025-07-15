# ==============================================================================
# ⚗️ test_parser_xml.py
#
# Descrição:
#     Teste unitário para a função extrair_loc_drawio do módulo parser_xml.py.
#     Verifica se o LOC retornado é um número inteiro positivo a partir de um 
#     arquivo XML de exemplo gerado pelo Draw.io.
#
# Autor: MOACYR ✍️
# Copilot: Microsoft 🤖
# ==============================================================================

import pytest
from modules.parser_xml import extrair_loc_drawio

def test_loc_estimada_xml():
    """
    Testa se o LOC estimado a partir de um XML UML é válido e positivo.
    """
    loc = extrair_loc_drawio("testes/modelo_xml_curto.xml")  # Arquivo de teste simplificado
    assert isinstance(loc, int)          # Verifica se é do tipo inteiro
    assert loc > 0                       # Verifica se é maior que zero
