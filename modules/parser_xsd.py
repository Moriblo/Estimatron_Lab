import xmlschema

def calcular_eaf_xsd(xsd_path):
    schema = xmlschema.XMLSchema(xsd_path)

    tipos_complexos = len(schema.types)
    profundidades = []

    def profundidade(el, nivel=0):
        filhos = list(el.type.content.iter_elements())
        if not filhos:
            return nivel
        return max([profundidade(f, nivel+1) for f in filhos])

    for el in schema.elements.values():
        try:
            p = profundidade(el)
            profundidades.append(p)
        except:
            continue

    profundidade_max = max(profundidades) if profundidades else 1

    # Fórmula simples de ajuste EAF
    eaf = 1.0 + (tipos_complexos * 0.01) + (profundidade_max * 0.05)
    return round(eaf, 2)
