###############################################################################
# cocomo_model.py
# 🧮 Estimatron - Modelo de cálculo COCOMO II
#
# Este módulo implementa uma versão simplificada do COCOMO II, utilizada
# para estimar esforço, prazo e custo de desenvolvimento com base em LOC,
# EAF (fator de ajuste de complexidade), e salário mensal informado.
#
# Autor: MOACYR + Copilot
# Versão: 1.2
# Data: 2025-07-15
###############################################################################

from typing import Tuple

def calcular_cocomo(loc: int, eaf: float, salario_mensal: float) -> Tuple[float, float, float]:
    """
    Calcula esforço, prazo e custo total de desenvolvimento baseado no modelo COCOMO II.

    Parâmetros:
        loc (int): Linhas de código estimadas (LOC).
        eaf (float): Fator de ajuste técnico (Effort Adjustment Factor).
        salario_mensal (float): Salário médio mensal da equipe em R$.

    Retorna:
        tuple:
            - esforco (float): Esforço em pessoa-mês.
            - prazo (float): Prazo estimado em meses.
            - custo_total (float): Custo total do projeto em reais.
    
    Exceções:
        ValueError: Se os parâmetros forem inválidos (negativos ou fora de faixa).
    """
    if not isinstance(loc, int) or loc < 0:
        raise ValueError("LOC deve ser um número inteiro não negativo.")
    if not isinstance(eaf, (int, float)) or eaf < 0.1:
        raise ValueError("EAF deve ser um número positivo.")
    if not isinstance(salario_mensal, (int, float)) or salario_mensal < 1000:
        raise ValueError("Salário mensal deve ser um valor numérico acima de R$1000.")

    # Parâmetros ajustáveis do modelo
    a = 2.94
    b = 0.91
    c = 3.67

    esforco = round(a * (loc / 1000) ** b * eaf, 2)
    prazo = round(c * esforco ** 0.35, 2)
    custo_total = round(esforco * salario_mensal, 2)

    return esforco, prazo, custo_total

