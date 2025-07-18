""" ############################################################################
parser_xsd.py
📂 Funções para analisar XSD e calcular fator de ajuste técnico (EAF)

Processa o esquema XML gerado a partir do modelo UML, calcula complexidade
baseada em elementos globais, internos e complexTypes.

Autor: MOACYR + Copilot
Versão: 2.0
################################################################################ """

import xml.etree.ElementTree as ET

def calcular_eaf_xsd(xsd_path):
    try:
        tree = ET.parse(xsd_path)
        root = tree.getroot()
    except Exception as e:
        return {
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

    # 🧠 Regra de faixa EAF baseada na complexidade
    if total < 5:
        faixa = 0.85  # projeto simples
    elif total <= 15:
        faixa = 1.00  # média complexidade
    else:
        faixa = 1.15  # alta complexidade

    return {
    "arquivo": xsd_path,  # ← nova chave
    "elementos_globais": len(globais),
    "elementos_internos": len(internos),
    "complex_types": len(tipos),
    "total_elementos": total,
    "eaf": faixa,
    "erro": None
    }
