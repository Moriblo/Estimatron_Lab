# ==============================================================================
# 📐 parser_xsd.py
#
# Descrição:
#     Este módulo é responsável por interpretar esquemas XML definidos via XSD 
#     (XML Schema Definition) e gerar um fator de ajuste técnico (EAF) com base 
#     na complexidade estrutural. Ele utiliza a biblioteca xmlschema para carregar 
#     o schema e avaliar características como número de elementos, tipos complexos 
#     e profundidade hierárquica.
#
#     O EAF gerado pode ser usado como multiplicador no modelo COCOMO II, indicando
#     o impacto da estrutura técnica do modelo sobre o esforço necessário.
#
# Autor: MOACYR ✍️
# Copilot: Microsoft 🤖
# ==============================================================================

import xmlschema

def calcular_eaf_xsd(caminho_arquivo_xsd):
    """
    Analisa a estrutura do arquivo XSD e calcula um fator de ajuste (EAF).

    Parâmetros:
        caminho_arquivo_xsd (str): Caminho para o arquivo XSD.

    Retorna:
        float: Fator técnico estimado entre 0.8 e 2.0 (EAF).
    """

    # 📂 Carrega o schema XSD
    schema = xmlschema.XMLSchema(caminho_arquivo_xsd)

    # 🧮 Contabiliza o número de elementos e tipos complexos
    num_elementos = len(schema.elements)
    num_tipos = len(schema.types)

    # 📈 Heurística simples para estimar complexidade técnica
    complexidade = num_elementos + num_tipos

    # ⚖️ Converte complexidade em fator EAF
    # Mínimo 0.8 (pouco complexo), máximo 2.0 (muito complexo)
    if complexidade < 10:
        eaf = 0.9
    elif complexidade < 30:
        eaf = 1.0
    elif complexidade < 60:
        eaf = 1.3
    else:
        eaf = 1.7

    return round(eaf, 2)

