"""
main.py
🎯 Estimatron - Interface Principal via Streamlit

Executa o estimador COCOMO II com entrada de arquivo XML exportado do draw.io.
O XSD é gerado automaticamente com base nos blocos textuais detectados.
Exibe diagnósticos técnicos e realiza estimativa completa.
Remove os arquivos temporários ao final do processo.

Autor: MOACYR + Copilot
Versão: 2.2
Data: 2025-07-15
"""

import streamlit as st
import os

from modules.parser_xml import extrair_loc_drawio
from modules.parser_xsd import calcular_eaf_xsd
from modules.cocomo_model import calcular_cocomo
from modules.validator_xml import validar_xml_drawio

# 🛠️ Geração automática do XSD com base nos blocos textuais
def gerar_xsd_basico(blocos, xsd_saida):
    with open(xsd_saida, "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0"?>\n')
        f.write('<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">\n')
        for nome in blocos:
            f.write(f'  <xs:element name="{nome}" type="xs:string"/>\n')
        f.write('</xs:schema>\n')

# 🧼 Função para remover arquivos temporários
def limpar_arquivos_temp():
    arquivos_temp = ["temp_modelo.xml", "temp_modelo.xsd"]
    for arquivo in arquivos_temp:
        if os.path.exists(arquivo):
            try:
                os.remove(arquivo)
            except Exception as e:
                print(f"[⚠️] Não foi possível remover '{arquivo}': {e}")

# 🎨 Interface do Streamlit
st.set_page_config(page_title="Estimativa COCOMO II", layout="centered")
st.title("📐 Estimador COCOMO II baseado em XML")
st.markdown("Carregue seu modelo UML exportado do draw.io para iniciar:")

# 📂 Upload do XML
xml_file = st.file_uploader("📂 Upload do modelo UML (XML)", type=["xml"])
salario = st.number_input("💰 Salário mensal (R$)", min_value=1000, value=12000)

if xml_file:
    with open("temp_modelo.xml", "wb") as f:
        f.write(xml_file.read())

    # 🔍 Diagnóstico técnico do XML
    diagnostico = validar_xml_drawio("temp_modelo.xml")

    st.markdown("### 🧪 Diagnóstico técnico do XML")
    st.write(f"📄 Arquivo: `{diagnostico['arquivo']}`")
    st.write(f"✅ Validade estrutural: **{'Válido' if diagnostico['valido'] else 'Inválido'}**")
    st.write(f"🏷️ Tipo de raiz detectada: `{diagnostico.get('tipo_raiz', 'Não identificada')}`")
    st.write(f"🔢 Total de células (mxCell): **{diagnostico['num_celulas']}**")
    st.write(f"✏️ Blocos com texto (LOC candidatos): **{diagnostico['num_blocos_com_texto']}**")
    if diagnostico["erro"]:
        st.error(f"❌ Erro detectado: {diagnostico['erro']}")

    # ✅ Definindo se dados estão prontos
    dados_validos = diagnostico["valido"] and diagnostico["num_blocos_com_texto"] > 0
    loc, eaf = 0, 1.00  # Defaults para segurança

    if dados_validos:
        resultado = extrair_loc_drawio("temp_modelo.xml")
        loc = resultado["loc"]
        blocos = resultado["blocos"]

        gerar_xsd_basico(blocos, "temp_modelo.xsd")
        eaf_info = calcular_eaf_xsd("temp_modelo.xsd")
        eaf = eaf_info["eaf"]

        st.markdown("### 🧪 Diagnóstico técnico do XSD gerado")
        st.write(f"📄 Arquivo: `temp_modelo.xsd`")
        st.write(f"🔢 Elementos globais: **{eaf_info['elementos_globais']}**")
        st.write(f"📂 Elementos internos: **{eaf_info['elementos_internos']}**")
        st.write(f"🧩 Módulos (complexTypes): **{eaf_info['complex_types']}**")
        st.write(f"🧮 Total de elementos: **{eaf_info['total_elementos']}**")
        st.write(f"📊 Faixa EAF atribuída: **{eaf}**")
    else:
        st.warning("⚠️ Arquivo XML não possui estrutura ou blocos textuais suficientes para estimativa.")

    # 🚀 Botão visível — execução condicionada
    if st.button("🚀 Gerar estimativa"):
        if dados_validos:
            esforco, prazo, custo = calcular_cocomo(loc, eaf, salario)
            st.success("✅ Estimativa concluída!")
            st.write(f"🔢 LOC estimado: **{loc}**")
            st.write(f"⚙️ Fator de ajuste EAF: **{eaf}**")
            st.write(f"🧠 Esforço estimado: **{esforco} pessoa-mês**")
            st.write(f"📆 Prazo estimado: **{prazo} meses**")
            st.write(f"💸 Custo total: **R${custo:.2f}**")

            limpar_arquivos_temp()
        else:
            st.error("❌ Estimativa não gerada. Verifique a estrutura do XML e os blocos detectados.")
