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

def calcular_eaf_xsd(caminho_arquivo):
    """
    Analisa um arquivo XSD e calcula o EAF (Fator de Ajuste de Complexidade),
    além de retornar estatísticas detalhadas da estrutura do schema.

    Retorna:
        dict: informações sobre o arquivo, incluindo total de elementos,
              módulos detectados e EAF atribuído.
    """
    try:
        schema = xmlschema.XMLSchema(caminho_arquivo)
    except xmlschema.XMLSchemaException as erro:
        print(f"❌ Erro ao carregar schema: {erro}")
        return {
            "arquivo": caminho_arquivo,
            "elementos_globais": 0,
            "elementos_internos": 0,
            "modulos": 0,
            "total_elementos": 0,
            "eaf": 0.0
        }

    elementos_globais = len(schema.elements)
    elementos_internos = 0
    modulos = len(schema.types)

    # Percorre todos os tipos complexos e soma elementos internos
    for tipo_nome, tipo_obj in schema.types.items():
        try:
            if tipo_obj.content:
                internos = [
                    c for c in tipo_obj.content.iter_elements()
                    if getattr(c, "name", None)
                ]
                elementos_internos += len(internos)
        except Exception as e:
            print(f"⚠️ Erro ao processar tipo '{tipo_nome}': {e}")

    total_elementos = elementos_globais + elementos_internos

    # Classifica o EAF conforme a complexidade estrutural
    if total_elementos < 10:
        eaf = 0.9
    elif total_elementos < 30:
        eaf = 1.0
    elif total_elementos < 60:
        eaf = 1.3
    else:
        eaf = 1.7

    return {
        "arquivo": caminho_arquivo,
        "elementos_globais": elementos_globais,
        "elementos_internos": elementos_internos,
        "modulos": modulos,
        "total_elementos": total_elementos,
        "eaf": round(eaf, 2)
    }
