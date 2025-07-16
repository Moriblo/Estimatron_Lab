"""
🎯 Estimatron - Interface Principal via Streamlit

Executa o estimador COCOMO II interativamente, com entrada manual de XML/XSD
ou via config.json. O cálculo é feito com base em LOC (modelo UML via draw.io)
e EAF (complexidade técnica via XSD). Exibe diagnósticos técnicos antes da estimativa.

Autor: MOACYR + Copilot
Versão: 1.2
Data: 2025-07-15
"""

import streamlit as st
import json
import os

from modules.parser_xml import extrair_loc_drawio
from modules.parser_xsd import calcular_eaf_xsd
from modules.cocomo_model import calcular_cocomo
from modules.validator_xml import validar_xml_drawio

# Configura a interface
st.set_page_config(page_title="Estimativa COCOMO II", layout="centered")
st.title("📐 Estimador COCOMO II baseado em UML/XML/XSD")
st.markdown("Escolha como deseja fornecer os dados:")

# Define modo de entrada
modo = st.radio("Entrada de parâmetros:", ["Manual", "Arquivo config.json"])

# === Entrada Manual ===
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

        # ⛓️ Segue para estimativa apenas se XML está válido e contém blocos
        if diagnostico["valido"] and diagnostico["num_blocos_com_texto"] > 0:
            loc = extrair_loc_drawio("temp_modelo.xml")
            eaf_info = calcular_eaf_xsd("temp_modelo.xsd")

            # 🧠 Diagnóstico técnico do XSD
            st.markdown("### 🧪 Diagnóstico técnico do XSD")
            st.write(f"📄 Arquivo: `temp_modelo.xsd`")
            st.write(f"🔢 Elementos globais: **{eaf_info['elementos_globais']}**")
            st.write(f"📂 Elementos internos: **{eaf_info['elementos_internos']}**")
            st.write(f"🧩 Módulos (complexTypes): **{eaf_info['complex_types']}**")
            st.write(f"🧮 Total de elementos: **{eaf_info['total_elementos']}**")
            st.write(f"📊 Faixa EAF atribuída: **{eaf_info['eaf']}**")

            eaf = eaf_info["eaf"]
            if st.button("🚀 Gerar estimativa"):
                esforco, prazo, custo = calcular_cocomo(loc, eaf, salario)

                st.success("✅ Estimativa concluída!")
                st.write(f"🔢 LOC estimado: **{loc}**")
                st.write(f"⚙️ Fator de ajuste EAF: **{eaf}**")
                st.write(f"🧠 Esforço estimado: **{esforco} pessoa-mês**")
                st.write(f"📆 Prazo estimado: **{prazo} meses**")
                st.write(f"💸 Custo total: **R${custo:.2f}**")

# === Entrada via config.json ===
else:
    st.subheader("📁 Entrada via arquivo config.json")
    config_file = st.file_uploader("📂 Upload do config.json", type=["json"])

    if config_file:
        config = json.load(config_file)
        xml_path = config.get("xml_path")
        xsd_path = config.get("xsd_path")
        salario = config.get("salario_mensal", 12000)

        if os.path.exists(xml_path) and os.path.exists(xsd_path):
            diagnostico = validar_xml_drawio(xml_path)

            st.markdown("### 🧪 Diagnóstico técnico do XML")
            st.write(f"📄 Arquivo: `{diagnostico['arquivo']}`")
            st.write(f"✅ Validade estrutural: **{'Válido' if diagnostico['valido'] else 'Inválido'}**")
            st.write(f"🏷️ Tipo de raiz detectada: `{diagnostico.get('tipo_raiz', 'Não identificada')}`")
            st.write(f"🔢 Total de células (mxCell): **{diagnostico['num_celulas']}**")
            st.write(f"✏️ Blocos com texto (LOC candidatos): **{diagnostico['num_blocos_com_texto']}**")
            if diagnostico["erro"]:
                st.error(f"❌ Erro detectado: {diagnostico['erro']}")

            if diagnostico["valido"] and diagnostico["num_blocos_com_texto"] > 0:
                loc = extrair_loc_drawio(xml_path)
                eaf_info = calcular_eaf_xsd(xsd_path)

                st.markdown("### 🧪 Diagnóstico técnico do XSD")
                st.write(f"📄 Arquivo: `{xsd_path}`")
                st.write(f"🔢 Elementos globais: **{eaf_info['elementos_globais']}**")
                st.write(f"📂 Elementos internos: **{eaf_info['elementos_internos']}**")
                st.write(f"🧩 Módulos (complexTypes): **{eaf_info['complex_types']}**")
                st.write(f"🧮 Total de elementos: **{eaf_info['total_elementos']}**")
                st.write(f"📊 Faixa EAF atribuída: **{eaf_info['eaf']}**")

                eaf = eaf_info["eaf"]
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
