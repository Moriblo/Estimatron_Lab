# ==============================================================================
# 🧠 cocomo_model.py
#
# Descrição:
#     Este módulo implementa o cálculo de estimativas para esforço, prazo e custo 
#     em projetos de software com base no modelo COCOMO II (Constructive Cost Model).
#     A função principal aplica fórmulas padrão da versão COCOMO II para:
#         - Esforço estimado em pessoa-mês
#         - Prazo do projeto em meses
#         - Custo total com base no salário mensal informado
#
# Utilização típica:
#     calcular_cocomo(loc_estimado, eaf_calculado, salario_mensal)
#
# Autor: MOACYR ✍️
# Copilot: Microsoft 🤖
# ==============================================================================

def calcular_cocomo(loc, eaf=1.0, salario_mensal=12000):
    """
    Estima esforço, prazo e custo de projeto de software usando o modelo COCOMO II.

    Parâmetros:
        loc (int): Linhas de código estimadas (Lines of Code).
        eaf (float): Fator de ajuste técnico (Effort Adjustment Factor). Default: 1.0.
        salario_mensal (float): Custo mensal por pessoa (R$). Default: R$12.000.

    Retorna:
        tuple: (esforco_pessoa_mes, prazo_meses, custo_total)
    """

    # Coeficientes do modelo COCOMO II para projetos orgânicos
    A = 2.94  # Fator multiplicador base
    B = 1.1   # Expoente de escala

    # 🔧 Cálculo do esforço total em pessoa-mês
    # Fórmula: esforço = A * (KLOC)^B * EAF
    # Onde KLOC = LOC / 1000
    esforco_pm = A * (loc / 1000) ** B * eaf

    # 📆 Estimativa de prazo do projeto (em meses)
    # Fórmula clássica: duration = 2.5 * (esforço)^0.38
    prazo_meses = 2.5 * (esforco_pm) ** 0.38

    # 💰 Cálculo do custo total com base no salário mensal informado
    custo_total = esforco_pm * salario_mensal

    # 🔙 Retorna os valores arredondados para apresentação
    return round(esforco_pm, 2), round(prazo_meses, 2), round(custo_total, 2)
