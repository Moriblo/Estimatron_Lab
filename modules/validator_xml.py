"""
validator_xml.py
🛡️ Validador XML especializado para modelos draw.io

Este módulo analisa um arquivo XML exportado pelo draw.io e retorna diagnóstico técnico
sobre estrutura, presença de namespace, número de células, blocos textuais e validade estrutural.

Critério de validade: o XML deve conter ao menos uma tag <mxGraphModel>,
mesmo que não esteja na raiz (permite raiz como <mxfile>).

Autor: MOACYR + Copilot
Versão: 2.2
Data: 2025-07-15
"""

import xml.etree.ElementTree as ET

def validar_xml_drawio(xml_path):
    """
    🔍 Valida um arquivo XML gerado pelo draw.io
    Retorna um dicionário com informações estruturais e semânticas úteis.

    Parâmetros:
        xml_path (str): Caminho para o arquivo XML a ser validado

    Retorno:
        dict: Diagnóstico técnico contendo:
            - valido (bool): Estrutura compatível com modelos do draw.io
            - erro (str | None): Mensagem de erro de parsing ou execução
            - tipo_raiz (str): Nome da tag raiz do XML
            - xmlns_detectado (bool): Se namespace está presente
            - num_celulas (int): Total de elementos <mxCell> encontrados
            - num_blocos_com_texto (int): Total de células com texto (LOC candidatos)
    """

    resultado = {
        "arquivo": xml_path,
        "valido": False,
        "erro": None,
        "num_celulas": 0,
        "num_blocos_com_texto": 0,
        "tipo_raiz": None,
        "xmlns_detectado": False,
    }

    try:
        # 🧠 Parse do arquivo XML
        tree = ET.parse(xml_path)
        root = tree.getroot()

        # 🎯 Tag raiz do documento
        resultado["tipo_raiz"] = root.tag

        # 🔍 Detecta se há namespace (xmlns ou xmlns:xlink)
        resultado["xmlns_detectado"] = "xmlns" in root.attrib or "xmlns:xlink" in root.attrib

        # 📌 Verifica se existe um elemento <mxGraphModel> na árvore inteira
        estrutura_minima = root.find(".//mxGraphModel") is not None
        resultado["valido"] = estrutura_minima

        # 📦 Busca todas as células gráficas (<mxCell>)
        celulas = root.findall(".//mxCell")
        resultado["num_celulas"] = len(celulas)

        # 🧮 Filtra blocos que têm texto (usado para estimar LOC)
        blocos_texto = [
            cel for cel in celulas
            if "value" in cel.attrib and cel.attrib["value"].strip()
        ]
        resultado["num_blocos_com_texto"] = len(blocos_texto)

    except ET.ParseError as e:
        resultado["erro"] = f"XML mal formado: {e}"
    except Exception as e:
        resultado["erro"] = f"Falha inesperada: {e}"

    return resultado
