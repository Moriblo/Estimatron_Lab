###############################################################################
# parser_xsd.py
# 📂 Funções para analisar XSD e calcular fator de ajuste técnico (EAF)
#
# Processa o esquema XML gerado a partir do modelo UML, calcula complexidade
# baseada em elementos globais, internos e complexTypes.
#
# Autor: MOACYR + Copilot
# Versão: 2.1
# Data: 2025-07-15
###############################################################################

from typing import Dict, Union
import xml.etree.ElementTree as ET

def calcular_eaf_xsd(xsd_path: str) -> Dict[str, Union[int, float, str, None]]:
    """
    Analisa um arquivo XSD gerado a partir de XML UML e calcula o EAF (Effort Adjustment Factor)
    com base na complexidade estrutural do schema.

    Parâmetros:
        xsd_path (str): Caminho do arquivo XSD a ser analisado.

    Retorna:
        dict: Um dicionário contendo:
            - 'arquivo' (str): Caminho analisado.
            - 'elementos_globais' (int): Elementos <xs:element> fora de complexTypes.
            - 'elementos_internos' (int): Elementos internos dentro de <xs:complexType>.
            - 'complex_types' (int): Total de blocos <xs:complexType>.
            - 'total_elementos' (int): Soma dos componentes analisados.
            - 'eaf' (float): Fator de esforço atribuído com base na complexidade.
            - 'erro' (str ou None): Mensagem de erro em caso de falha.
    """
    try:
        tree = ET.parse(xsd_path)
        root = tree.getroot()
    except Exception as e:
        return {
            "arquivo": xsd_path,
            "elementos_globais": 0,
            "elementos_internos": 0,
            "complex_types": 0,
            "total_elementos": 0,
            "eaf": 1.00,
            "erro": f"Falha ao analisar XSD: {str(e)}"
        }

    ns = {"xs": "http://www.w3.org/2001/XMLSchema"}
    globais = root.findall(".//xs:element", ns)
    internos = root.findall(".//xs:complexType//xs:element", ns)
    tipos = root.findall(".//xs:complexType", ns)

    total = len(globais) + len(internos) + len(tipos)

    # 🧠 Faixa de complexidade → EAF
    if total < 5:
        faixa = 0.85
    elif total <= 15:
        faixa = 1.00
    else:
        faixa = 1.15

    return {
        "arquivo": xsd_path,
        "elementos_globais": len(globais),
        "elementos_internos": len(internos),
        "complex_types": len(tipos),
        "total_elementos": total,
        "eaf": faixa,
        "erro": None
    }

