"""
🧪 Testes para o módulo validator_xml.py

Valida a robustez do analisador estrutural de arquivos XML exportados do draw.io.
Verifica se o validador identifica corretamente arquivos bem formados, inválidos
ou sem conteúdo útil para análise LOC.

Autor: MOACYR + Copilot
Versão: 1.0
Data: 2025-07-15
"""

import os
import pytest
from modules.validator_xml import validar_xml_drawio

# === Arquivo válido ===
def test_xml_valido():
    resultado = validar_xml_drawio("testes/xml_exemplo_valido.xml")
    assert resultado["valido"]
    assert resultado["contém_mxGraphModel"]
    assert resultado["num_blocos_com_texto"] > 0

# === Arquivo malformado (sintaxe quebrada) ===
def test_xml_malformado():
    resultado = validar_xml_drawio("testes/xml_malformado.xml")
    assert not resultado["valido"]
    assert "XML mal formado" in resultado["erro"]

# === Arquivo vazio ===
def test_xml_vazio():
    resultado = validar_xml_drawio("testes/xml_vazio.xml")
    assert not resultado["valido"]
    assert "XML mal formado" in resultado["erro"] or "Falha inesperada" in resultado["erro"]

# === Arquivo sem células com texto ===
def test_xml_sem_blocos():
    resultado = validar_xml_drawio("testes/xml_sem_blocos.xml")
    assert resultado["valido"]
    assert resultado["num_blocos_com_texto"] == 0
