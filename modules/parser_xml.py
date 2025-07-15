# ==============================================================================
# 📄 parser_xml.py
#
# Descrição:
#     Este módulo realiza a análise de arquivos XML exportados do Draw.io contendo
#     diagramas UML. A função principal extrai elementos como blocos, conectores ou
#     nós relevantes para estimar a quantidade total de linhas de código (LOC).
#
#     A lógica é baseada na contagem de elementos estruturais (por exemplo, retângulos)
#     que representariam classes, entidades ou componentes no projeto, atribuindo
#     estimativas médias de LOC por elemento.
#
# Autor: MOACYR ✍️
# Copilot: Microsoft 🤖
# ==============================================================================

import xml.etree.ElementTree as ET

def extrair_loc_drawio(caminho_arquivo_xml):
    """
    Lê um arquivo XML do Draw.io contendo o modelo UML e estima o LOC total.

    Parâmetros:
        caminho_arquivo_xml (str): Caminho para o arquivo XML exportado do Draw.io.

    Retorna:
        int: Estimativa de linhas de código com base no número de elementos encontrados.
    """

    # 📂 Carrega e interpreta o XML via ElementTree
    arvore = ET.parse(caminho_arquivo_xml)
    raiz = arvore.getroot()

    # 🔍 Busca todos os elementos 'mxCell' representando figuras UML no Draw.io
    elementos = raiz.findall(".//mxCell")

    # 🧮 Filtra e conta apenas aqueles que têm 'value' (ignorando conectores e metadados)
    elementos_com_valor = [el for el in elementos if el.get("value")]

    # 📏 Define uma estimativa média de LOC por elemento detectado
    loc_por_elemento = 20  # Pode ser calibrado conforme o domínio

    # 📊 Cálculo total estimado
    loc_total = len(elementos_com_valor) * loc_por_elemento

    return loc_total

