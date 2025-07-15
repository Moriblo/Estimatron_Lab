import xml.etree.ElementTree as ET

def extrair_loc_drawio(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    elements = root.findall(".//mxCell")

    class_count = 0
    attribute_count = 0

    for elem in elements:
        style = elem.attrib.get("style", "")
        value = elem.attrib.get("value", "")

        if "shape=umlClass" in style:
            class_count += 1
            attribute_count += value.count("<br>") if value else 0

    loc = class_count * 50 + attribute_count * 10
    return loc
