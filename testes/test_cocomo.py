# ==============================================================================
# ⚗️ test_cocomo.py
#
# Descrição:
#     Teste unitário para a função calcular_cocomo do módulo cocomo_model.py.
#     Verifica se os valores de esforço, prazo e custo são positivos e coerentes.
#
# Autor: MOACYR ✍️
# Copilot: Microsoft 🤖
# ==============================================================================

import pytest
from modules.cocomo_model import calcular_cocomo

def test_cocomo_estimativa_basica():
    """
    Testa se a estimativa gerada pela função está dentro de parâmetros aceitáveis.
    """
    loc = 1000             # LOC de entrada
    eaf = 1.0              # Fator neutro
    salario = 12000        # Salário padrão

    esforco, prazo, custo = calcular_cocomo(loc, eaf, salario)

    assert esforco > 0     # Verifica se esforço é positivo
    assert prazo > 0       # Verifica se prazo é positivo
    assert custo == round(esforco * salario, 2)  # Custo calculado corretamente
