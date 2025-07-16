"""
parser_xml.py
📄 Funções para processar modelo UML exportado do draw.io (XML)

Inclui extração de blocos textuais e cálculo de LOC.
Retorna estrutura reutilizável para geração automática do XSD.

Autor: MOACYR + Copilot
Versão: 2.0
"""

import xml.etree.ElementTree as ET

def extrair_loc_drawio(xml_path):
    """
    Analisa um arquivo XML exportado do draw.io
    Retorna:
    - loc: quantidade de blocos com texto
    - blocos: lista de strings (valores textuais dos blocos)
    """
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
    except Exception as e:
        return {
            "loc": 0,
            "blocos": [],
            "erro": f"Falha ao analisar XML: {str(e)}"
        }

    blocos = []
    for cell in root.iter("mxCell"):
        valor = cell.attrib.get("value", "").strip()
        if valor:
            blocos.append(valor)

    return {
        "loc": len(blocos),
        "blocos": blocos
    }