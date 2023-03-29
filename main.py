from RpaWpp import WppSender
import time
import pandas as pd
import streamlit as st

# --- FRONT-END ----
st.set_page_config(
    page_title="Projeto RPA - WhatsApp",
    page_icon="📫",
    layout="centered"
)

with open("styles.css","r") as css_file:
    st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)

st.header("📫 Projeto RPA - WhatsApp")
st.markdown(
    """
    O presente projeto consistiu em criar um RPA para envio de mensagens simples de texto via WhatsApp utilizando uma interface gráfica que simula um site.
    #####
    """
)

with st.form("forms"):
    st.markdown("#### • Preencha os campos abaixo:")
    message_text = st.text_area("Mensagem que deseja enviar:", max_chars=250, placeholder="Digite sua mensagem automática")
    st.markdown("#####")
    uploaded_file = st.file_uploader(
        label="Faça o upload do seu arquivo de contatos:",
        type=["xlsx"],
        accept_multiple_files=False,
    )
    st.markdown("#####")
    st.form_submit_button("Iniciar", type="primary")

# --- BACK-END ----
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    df["CONTATO"] = df["CONTATO"].astype("str")
    
    user = WppSender(headless=False)
    user.get_wpp_site()
    user.send_messages(message_text, df["CONTATO"])

    success = st.success("Mensagens enviadas com sucesso!", icon="✅")
    st.balloons()
    time.sleep(5)
    success.empty()