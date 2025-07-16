""" #############################################################################
test_cocomo.py
🧮 Testes unitários — Modelo de cálculo COCOMO II

Valida a função `calcular_cocomo()` com parâmetros válidos e inválidos.
Inclui testes de exceções para LOC negativo, EAF fora da faixa e salário muito baixo.

Autor: MOACYR + Copilot
Versão da suíte de testes: 2.2
Data: 2025-07-17
################################################################################# """

import pytest
from modules.cocomo_model import calcular_cocomo

# ✅ Entrada válida retorna resultados numéricos positivos
def test_cocomo_valido():
    esforco, prazo, custo = calcular_cocomo(2000, 1.0, 8000)
    assert esforco > 0
    assert prazo > 0
    assert custo > 0

# ❌ LOC negativo deve disparar exceção
def test_loc_negativo():
    with pytest.raises(ValueError):
        calcular_cocomo(-10, 1.0, 8000)

# ❌ EAF abaixo de 0.1 não permitido
def test_eaf_invalido():
    with pytest.raises(ValueError):
        calcular_cocomo(5000, 0.01, 8000)

# ❌ Salário mensal abaixo de R$1000 deve causar erro
def test_salario_muito_baixo():
    with pytest.raises(ValueError):
        calcular_cocomo(5000, 1.0, 500)

