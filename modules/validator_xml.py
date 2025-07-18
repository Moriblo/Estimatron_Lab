###############################################################################
# validator_xml.py
# 🛡️ Validador XML especializado para modelos draw.io
#
# Analisa um arquivo XML exportado pelo draw.io e retorna diagnóstico técnico
# sobre estrutura, presença de namespace, número de células, blocos textuais
# e validade estrutural do modelo.
#
# Critério de validade: o XML deve conter ao menos uma tag <mxGraphModel>,
# mesmo que não esteja na raiz (permite raiz como <mxfile>).
#
# Autor: MOACYR + Copilot
# Versão: 2.3
# Data: 2025-07-15
###############################################################################

from typing import Dict, Union
import xml.etree.ElementTree as ET

def validar_xml_drawio(xml_path: str) -> Dict[str, Union[str, int, bool, None]]:
    """
    Valida um arquivo XML gerado pelo draw.io e extrai diagnóstico técnico da estrutura.

    Parâmetros:
        xml_path (str): Caminho completo para o arquivo XML a ser validado.

    Retorna:
        dict: Diagnóstico contendo:
            - 'arquivo' (str): Caminho analisado.
            - 'valido' (bool): True se houver <mxGraphModel> no XML.
            - 'erro' (str ou None): Mensagem de erro, se aplicável.
            - 'tipo_raiz' (str): Tag raiz do documento.
            - 'xmlns_detectado' (bool): True se contiver namespace na raiz.
            - 'num_celulas' (int): Total de tags <mxCell> encontradas.
            - 'num_blocos_com_texto' (int): Total de células com atributo de texto.
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
        tree = ET.parse(xml_path)
        root = tree.getroot()

        resultado["tipo_raiz"] = root.tag
        resultado["xmlns_detectado"] = "xmlns" in root.attrib or "xmlns:xlink" in root.attrib

        resultado["valido"] = root.find(".//mxGraphModel") is not None

        celulas = root.findall(".//mxCell")
        resultado["num_celulas"] = len(celulas)

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

