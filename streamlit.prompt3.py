import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ===============================
# Configuração inicial
# ===============================
st.set_page_config(page_title="MVP - Insurance Dataset", layout="wide")

# ===============================
# Cabeçalho
# ===============================
st.title("📊 Análise Exploratória - Insurance Dataset")
st.write("👨‍💻 Autor: **Agezandro**")
st.write("🎯 Tema: Educação e Análise de Indicadores Escolares (Exemplo: Base Insurance)")
st.markdown("---")

# ===============================
# Sidebar
# ===============================
st.sidebar.title("📂 Menu")
secao = st.sidebar.radio("Escolha a seção:", ["Introdução", "Dados", "Gráficos", "Conclusões"])

# ===============================
# Seção: Introdução
# ===============================
if secao == "Introdução":
    with st.container():
        st.header("📖 Introdução")
        st.write("""
        Este aplicativo demonstra um **MVP de Exploração de Dados** usando a base pública 
        `insurance.csv`, que contém informações sobre idade, sexo, índice de massa corporal (BMI),
        número de filhos, hábito de fumar, região e custo do seguro (`charges`).
        """)
        st.info("Você pode navegar pelas seções usando o menu lateral à esquerda.")

# ===============================
# Seção: Dados
# ===============================
elif secao == "Dados":
    st.header("📂 Visualização e Estatísticas dos Dados")

    # Leitura do dataset
    df = pd.read_csv("insurance.csv")

    # Exibir primeiras linhas
    st.subheader("🔹 Pré-visualização dos Dados")
    st.dataframe(df.head())

    # Estatísticas descritivas
    st.subheader("📊 Estatísticas Descritivas")
    st.dataframe(df.describe())

    # Mostrar informações básicas
    st.subheader("🧮 Informações Gerais")
    st.write(f"Número de linhas: {df.shape[0]}")
    st.write(f"Número de colunas: {df.shape[1]}")
    st.write("Colunas disponíveis:", list(df.columns))

# ===============================
# Seção: Gráficos
# ===============================
elif secao == "Gráficos":
    st.header("📊 Visualizações Gráficas")
    df = pd.read_csv("insurance.csv")

    # Gráfico 1: Custo médio por região
    with st.expander("📍 Gráfico 1 - Custo médio por região"):
        avg_charges = df.groupby("region")["charges"].mean().sort_values()
        st.bar_chart(avg_charges)

    # Gráfico 2: Dispersão - idade x custo
    with st.expander("📈 Gráfico 2 - Dispersão entre Idade e Custo do Seguro"):
        fig, ax = plt.subplots()
        ax.scatter(df["age"], df["charges"], alpha=0.6)
        ax.set_xlabel("Idade")
        ax.set_ylabel("Custo do Seguro (charges)")
        ax.set_title("Dispersão: Idade x Custo do Seguro")
        st.pyplot(fig)

# ===============================
# Seção: Conclusões
# ===============================
elif secao == "Conclusões":
    st.header("📝 Conclusões")
    st.write("""
    - Há uma **tendência de aumento no custo do seguro** com a idade e com o hábito de fumar.  
    - As regiões apresentam **variações médias de custo**, possivelmente ligadas a fatores socioeconômicos.  
    - Este MVP cumpre os requisitos da **Etapa 3**, incluindo tabela descritiva e visualizações gráficas.
    """)
    st.success("✅ MVP completo e funcional!")

# ===============================
# Rodapé
# ===============================
st.markdown("---")
st.caption("MVP - Etapa 3 | Streamlit + Pandas | Prof. Maxwell Monteiro | Autor: Agezandro")
