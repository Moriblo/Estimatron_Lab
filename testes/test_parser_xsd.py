# ==============================================================================
# ⚗️ test_parser_xsd.py
#
# Descrição:
#     Testes unitários para a função calcular_eaf_xsd do módulo parser_xsd.py.
#     Utiliza arquivos XSD com níveis variados de complexidade e compara o EAF 
#     retornado com os valores esperados.
#
# Autor: MOACYR ✍️
# Copilot: Microsoft 🤖
# ==============================================================================

import pytest
from modules.parser_xsd import calcular_eaf_xsd

@pytest.mark.parametrize("arquivo_xsd, eaf_esperado", [
    ("testes/xsd_simples.xsd", 0.9),          # Caso: baixa complexidade
    ("testes/xsd_medio.xsd", 1.0),            # Caso: média complexidade
    ("testes/xsd_intermediario.xsd", 1.3),    # Caso: complexidade intermediária
    ("testes/xsd_complexo.xsd", 1.7),         # Caso: alta complexidade
])
def test_eaf_xsd(arquivo_xsd, eaf_esperado):
    """
    Testa se o fator EAF calculado para cada XSD corresponde ao esperado.
    """
    eaf = calcular_eaf_xsd(arquivo_xsd)
    assert eaf == eaf_esperado  # Compara com o valor definido na parametrização
