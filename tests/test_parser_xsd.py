"""#######################################################################
test_parser_xsd.py
🧬 Testes unitários — Análise estrutural de arquivos XSD

Verifica contagem de elementos globais, internos e tipos complexos.
Compara EAF calculado com valores esperados e testa tratamento de erros.

Autor: MOACYR + Copilot
Versão da suíte de testes: 2.2
Data: 2025-07-17
###########################################################################"""

import pytest
from modules.parser_xsd import calcular_eaf_xsd

# ✅ Testa diferentes faixas de complexidade de XSD e seus EAFs
@pytest.mark.parametrize("arquivo_xsd, eaf_esperado", [
    ("tests/xsd_simples.xsd", 0.85),
    ("tests/xsd_medio.xsd", 1.15),
    ("tests/xsd_intermediario.xsd", 1.15),
    ("tests/xsd_complexo.xsd", 1.15),
])
def test_eaf_xsd(arquivo_xsd, eaf_esperado):
    info = calcular_eaf_xsd(arquivo_xsd)
    print("\n📁 Diagnóstico do arquivo:", info["arquivo"])
    print(f"🔢 Elementos globais:       {info['elementos_globais']}")
    print(f"📂 Elementos internos:      {info['elementos_internos']}")
    print(f"🧩 Módulos (complexTypes):  {info['complex_types']}")
    print(f"🧮 Total de elementos:      {info['total_elementos']}")
    print(f"📊 Faixa EAF atribuída:     {info['eaf']}")
    assert info["eaf"] == eaf_esperado

# ❌ Arquivo inexistente deve retornar erro e total neutro
def test_arquivo_xsd_inexistente():
    resultado = calcular_eaf_xsd("tests/arquivo_fantasma.xsd")
    assert resultado["erro"] is not None
    assert resultado["total_elementos"] == 0
    assert resultado["eaf"] == 1.00

"""
❌ Testa comportamento ao tentar analisar um XSD malformado.
Espera-se que a função capture a exceção, retorne erro explícito
e atribua faixa EAF padrão de 1.00.
"""
def test_xsd_erro_de_parsing():
    resultado = calcular_eaf_xsd("tests/xsd_malformado.xsd")  # arquivo com tag quebrada
    assert resultado["erro"] is not None
    assert resultado["eaf"] == 1.00
    assert resultado["total_elementos"] == 0

"""
❌ Testa falha de parsing crítica com sintaxe XML irreparável.
Garante que o bloco 'except Exception' seja acionado.
"""
def test_xsd_malformado_fatal():
    resultado = calcular_eaf_xsd("tests/xsd_malformado_fatal.xsd")
    assert resultado["erro"] is not None
    assert resultado["eaf"] == 1.00
    assert resultado["total_elementos"] == 0

