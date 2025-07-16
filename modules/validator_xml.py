"""
validator_xml.py
🔍 Validador estrutural de arquivos XML exportados do draw.io

Suporta múltiplas versões e variações de estrutura geradas pela ferramenta,
identificando células gráficas e validando presença de blocos textuais úteis
para estimativa LOC.

Autor: MOACYR + Copilot
Versão: 1.2
Data: 2025-07-16
"""

import xml.etree.ElementTree as ET

def validar_xml_drawio(xml_path):
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

        # ✅ Verificação de estrutura mínima
        if root.tag != "mxGraphModel":
            resultado["valido"] = False
        else:
            resultado["valido"] = True

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
