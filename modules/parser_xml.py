"""
📦 Estimatron - Extrator LOC para arquivos XML (modelo UML do draw.io)

Este módulo analisa o XML exportado via draw.io e estima o número de linhas
de código (LOC) com base no número de blocos textuais identificados.

Agora inclui validação estrutural e suporte a múltiplas versões do XML.

Autor: MOACYR + Copilot
Versão: 1.1
Data: 2025-07-15
"""

import xml.etree.ElementTree as ET
from modules.validator_xml import validar_xml_drawio


def extrair_loc_drawio(caminho_arquivo):
    """
    Analisa o arquivo XML e estima LOC com base em blocos visíveis.

    Retorna:
        int: LOC estimado com base no número de blocos textuais.
    """
    # Valida antes de extrair
    diagnostico = validar_xml_drawio(caminho_arquivo)

    if not diagnostico["valido"]:
        print(f"❌ XML inválido: {diagnostico['erro']}")
        return 0

    if diagnostico["num_blocos_com_texto"] == 0:
        print("⚠️ Nenhum bloco com texto foi detectado. LOC será zero.")
        return 0

    print(f"📄 Diagnóstico draw.io: {diagnostico['num_blocos_com_texto']} blocos textuais encontrados.")
    return diagnostico["num_blocos_com_texto"]
