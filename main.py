import streamlit as st
import json
import os

from modules.parser_xml import extrair_loc_drawio
from modules.parser_xsd import calcular_eaf_xsd
from modules.cocomo_model import calcular_cocomo

st.set_page_config(page_title="Estimativa COCOMO II", layout="centered")
st.title("📐 Estimador COCOMO II baseado em UML/XML/XSD")

st.markdown("Escolha como deseja fornecer os dados:")

modo = st.radio("Entrada de parâmetros:", ["Manual", "Arquivo config.json"])

if modo == "Manual":
    st.subheader("📝 Entrada manual")

    xml_file = st.file_uploader("📂 Upload do modelo UML (XML)", type=["xml"])
    xsd_file = st.file_uploader("📂 Upload do XSD", type=["xsd"])

    salario = st.number_input("💰 Salário mensal (R$)", min_value=1000, value=12000)
    
    if xml_file and xsd_file:
        with open("temp_modelo.xml", "wb") as f:
            f.write(xml_file.read())
        with open("temp_modelo.xsd", "wb") as f:
            f.write(xsd_file.read())
            
        loc = extrair_loc_drawio("temp_modelo.xml")
        eaf = calcular_eaf_xsd("temp_modelo.xsd")
        
        if st.button("🚀 Gerar estimativa"):
            esforco, prazo, custo = calcular_cocomo(loc, eaf, salario)

            st.success("✅ Estimativa concluída!")
            st.write(f"🔢 LOC estimado: **{loc}**")
            st.write(f"⚙️ Fator de ajuste EAF: **{eaf}**")
            st.write(f"🧠 Esforço estimado: **{esforco} pessoa-mês**")
            st.write(f"📆 Prazo estimado: **{prazo} meses**")
            st.write(f"💸 Custo total: **R${custo:.2f}**")

else:
    st.subheader("📁 Entrada via arquivo config.json")

    config_file = st.file_uploader("📂 Upload do config.json", type=["json"])

    if config_file:
        config = json.load(config_file)
        xml_path = config.get("xml_path")
        xsd_path = config.get("xsd_path")
        salario = config.get("salario_mensal", 12000)

        if os.path.exists(xml_path) and os.path.exists(xsd_path):
            loc = extrair_loc_drawio(xml_path)
            eaf = calcular_eaf_xsd(xsd_path)

            if st.button("🚀 Gerar estimativa"):
                esforco, prazo, custo = calcular_cocomo(loc, eaf, salario)

                st.success("✅ Estimativa concluída!")
                st.write(f"🔢 LOC estimado: **{loc}**")
                st.write(f"⚙️ Fator de ajuste EAF: **{eaf}**")
                st.write(f"🧠 Esforço estimado: **{esforco} pessoa-mês**")
                st.write(f"📆 Prazo estimado: **{prazo} meses**")
                st.write(f"💸 Custo total: **R${custo:.2f}**")
        else:
            st.error("❌ Caminho para XML ou XSD inválido no config.json.")
