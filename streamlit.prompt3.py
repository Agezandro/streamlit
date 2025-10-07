import streamlit as st

# Configuração inicial
st.set_page_config(page_title="App Estrutura - Etapa 1", layout="wide")

# ===============================
# Cabeçalho
# ===============================
st.title("📊 Meu Web App - Estrutura Inicial")
st.write("👨‍💻 Autor: Agezandro")
st.write("🎯 Tema: Educação e Análise de Indicadores Escolares")

# ===============================
# Layout: Sidebar
# ===============================
st.sidebar.title("📂 Menu")
secao = st.sidebar.radio("Escolha a seção:", ["Introdução", "Dados", "Gráficos", "Conclusões"])

# ===============================
# Containers principais
# ===============================
if secao == "Introdução":
    with st.container():
        st.header("📖 Introdução")
        st.write("Aqui ficará o texto de introdução sobre o tema do app.")

elif secao == "Dados":
    col1, col2 = st.columns(2)  # exemplo de layout em colunas
    with col1:
        st.subheader("📂 Upload de Dados")
        st.write("Espaço reservado para upload de arquivos (CSV/Excel).")
    with col2:
        st.subheader("📋 Pré-visualização")
        st.write("Aqui será exibida a tabela carregada futuramente.")

elif secao == "Gráficos":
    with st.expander("📊 Gráfico 1: Histograma"):
        st.write("Espaço reservado para gráfico 1.")
    with st.expander("📈 Gráfico 2: Série Temporal"):
        st.write("Espaço reservado para gráfico 2.")

elif secao == "Conclusões":
    with st.container():
        st.header("📝 Conclusões")
        st.write("Resumo dos resultados e próximos passos.")

# Rodapé
st.markdown("---")
st.caption("Versão inicial - Estrutura simples sem dados")
