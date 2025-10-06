import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ===================================
# 1) Cabeçalho com nome e tema
# ===================================
st.set_page_config(page_title="Meu Primeiro App Streamlit", layout="wide")

st.title("📊 Meu Web App em Streamlit")
st.write("👨‍💻 Autor: **Agezandro Frederich Pratti**")
st.write("🎯 Tema: **Análise Educacional com Dados do IDEB**")

# ===================================
# 2) Estrutura de seções
# ===================================
menu = st.sidebar.radio("📂 Seções", ["Introdução", "Carregar Planilha", "Visualizar Dados", "Gráficos", "Conclusões"])

# ===================================
# 3) Introdução
# ===================================
if menu == "Introdução":
    st.header("📖 Introdução")
    st.write("""
    Este aplicativo demonstra como usar **Streamlit** para análise de dados educacionais.
    
    🔹 O usuário pode carregar uma planilha (Excel ou CSV).  
    🔹 Os dados serão exibidos em tabela.  
    🔹 Gráficos interativos ajudam a interpretar os resultados.  
    """)

# ===================================
# 4) Upload ou leitura de planilha
# ===================================
elif menu == "Carregar Planilha":
    st.header("📂 Carregar Planilha")
    uploaded_file = st.file_uploader("Escolha um arquivo CSV ou Excel", type=["csv", "xlsx"])

    if uploaded_file:
        try:
            if uploaded_file.name.endswith(".csv"):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)

            st.session_state["df"] = df  # guarda no estado da sessão
            st.success("✅ Planilha carregada com sucesso!")
            st.dataframe(df.head())

        except Exception as e:
            st.error(f"Erro ao ler arquivo: {e}")

# ===================================
# 5) Visualizar Dados
# ===================================
elif menu == "Visualizar Dados":
    st.header("📋 Visualizar Dados")
    if "df" in st.session_state:
        df = st.session_state["df"]

        st.subheader("🔹 Primeiras linhas")
        st.dataframe(df.head())

        st.subheader("🔹 Informações estatísticas")
        st.write(df.describe())

        st.subheader("🔹 Colunas disponíveis")
        st.write(list(df.columns))
    else:
        st.warning("⚠️ Nenhuma planilha carregada. Vá em **Carregar Planilha** primeiro.")

# ===================================
# 6) Gráficos
# ===================================
elif menu == "Gráficos":
    st.header("📊 Gráficos")
    if "df" in st.session_state:
        df = st.session_state["df"]

        coluna_numerica = st.selectbox("Escolha uma coluna numérica", df.select_dtypes(include="number").columns)

        if coluna_numerica:
            st.subheader(f"Histograma da coluna: {coluna_numerica}")
            fig, ax = plt.subplots()
            ax.hist(df[coluna_numerica].dropna(), bins=20, color="skyblue", edgecolor="black")
            ax.set_xlabel(coluna_numerica)
            ax.set_ylabel("Frequência")
            st.pyplot(fig)

            st.subheader(f"Série temporal (se aplicável) - {coluna_numerica}")
            st.line_chart(df[coluna_numerica].dropna().reset_index(drop=True))
    else:
        st.warning("⚠️ Nenhuma planilha carregada. Vá em **Carregar Planilha** primeiro.")

# ===================================
# 7) Conclusões
# ===================================
elif menu == "Conclusões":
    st.header("📝 Conclusões")
    st.write("""
    ✅ Este é um exemplo inicial de aplicativo com Streamlit.  
    📂 Ele suporta **upload de planilhas** (CSV/Excel).  
    📊 Permite **visualização de tabelas e gráficos**.  
    🚀 Pode ser expandido para análises educacionais reais.  
    """)
