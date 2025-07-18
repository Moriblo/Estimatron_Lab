###############################################################################
# parser_xml.py
# 📄 Funções para processar modelo UML exportado do draw.io (XML)
#
# Inclui extração de blocos textuais e cálculo de LOC.
# Retorna estrutura reutilizável para geração automática do XSD.
#
# Autor: MOACYR + Copilot
# Versão: 2.1
# Data: 2025-07-15
###############################################################################

from typing import List, Dict, Union
import xml.etree.ElementTree as ET

def extrair_loc_drawio(xml_path: str) -> Dict[str, Union[int, List[str], str, None]]:
    """
    Analisa um arquivo XML exportado do draw.io e extrai blocos textuais que
    representam candidatos a contagem de linhas de código (LOC).

    Parâmetros:
        xml_path (str): Caminho do arquivo XML a ser processado.

    Retorna:
        dict: Um dicionário com as seguintes chaves:
            - 'loc' (int): Total de blocos textuais detectados.
            - 'blocos' (List[str]): Lista contendo os textos dos blocos.
            - 'erro' (str ou None): Mensagem de erro, caso a análise falhe.
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
        "blocos": blocos,
        "erro": None
    }

