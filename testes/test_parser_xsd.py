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
    ("testes/xsd_simples.xsd", 0.9),
    ("testes/xsd_medio.xsd", 1.0),
    ("testes/xsd_intermediario.xsd", 1.3),
    ("testes/xsd_complexo.xsd", 1.7),
])
def test_eaf_xsd(arquivo_xsd, eaf_esperado):
    """
    Testa se o fator EAF calculado para cada XSD corresponde ao esperado
    e imprime diagnóstico detalhado da estrutura do schema.
    """
    info = calcular_eaf_xsd(arquivo_xsd)

    print("\n📁 Diagnóstico do arquivo:", info["arquivo"])
    print(f"🔢 Elementos globais:       {info['elementos_globais']}")
    print(f"📂 Elementos internos:      {info['elementos_internos']}")
    print(f"🧩 Módulos (complexTypes):  {info['modulos']}")
    print(f"🧮 Total de elementos:      {info['total_elementos']}")
    print(f"📊 Faixa EAF atribuída:     {info['eaf']}")

    assert info["eaf"] == eaf_esperado
