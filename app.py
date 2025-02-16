import streamlit as st
import pandas as pd
import plotly.express as px  # Importar plotly para los gráficos interactivos

# Leer datos
titanic = pd.read_csv("titanic.csv")

# Crear un gráfico con Plotly (por ejemplo, un gráfico de barras de la edad)
fig = px.histogram(titanic, x="age")

# Configuración de la página
st.set_page_config(page_title="Dashboard", layout="wide")
st.sidebar.title("Análisis de datos")

# Pestañas
tab1, tab2 = st.tabs(["Cuadros de desglose", "Gráficas"])

# Pestaña 1
with tab1:
    st.header("Información general")
    st.write(titanic.head())  # Usamos st.write() para mostrar el DataFrame
    st.write(titanic.info())  # Usamos st.write() para mostrar el resumen

# Pestaña 2
with tab2:
    selected_asset = st.selectbox("Seleccione un activo para analizar:", simbolos)
    # Mostrar el gráfico interactivo en Streamlit
    fig = px.histogram(titanic, x="age")
    st.plotly_chart(fig)


