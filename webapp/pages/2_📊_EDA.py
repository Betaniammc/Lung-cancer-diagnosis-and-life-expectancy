import streamlit as st
import pandas as pd
import os
from utils import set_design

# CONFIGURACIÓN ÚNICA
st.set_page_config(page_title="Análisis de Datos - EDA", layout="wide")
set_design("eda")

st.title("Exploración de Datos (EDA)")

# Carga de datos
st.sidebar.header("Configuración de Datos")
uploaded_file = st.sidebar.file_uploader("Sube tu archivo CSV", type=["csv"])

# --- LÓGICA DE RUTAS DINÁMICA ---
df = None

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("Archivo subido con éxito.")
else:
    # 1. Obtenemos la raíz del proyecto (subiendo un nivel desde la carpeta 'pages')
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # 2. Definimos la ruta exacta según tu estructura: raíz -> data -> processed
    ruta_auto = os.path.join(BASE_DIR, "data", "processed", "EDA_FINAL.csv")
    
    # 3. Lista de rutas de respaldo por si acaso
    rutas_respaldo = [
        ruta_auto,
        "data/processed/EDA_FINAL.csv",
        "webapp/data/EDA_FINAL.csv",
        "data/EDA_FINAL.csv"
    ]
    
    for ruta in rutas_respaldo:
        if os.path.exists(ruta):
            df = pd.read_csv(ruta)
            st.info(f"✅ Cargado automáticamente desde: {ruta}")
            break

    if df is None:
        st.warning("⚠️ No se encontró el dataset predeterminado.")

# --- VISUALIZACIÓN EN DATAFRAME [2026-02-12] ---
if df is not None:
    st.subheader("Vista general del Dataset")
    st.dataframe(df.head(10), use_container_width=True)

    st.subheader("Análisis Estadístico")
    # Formato DF solicitado: transponemos describe() para mejor lectura
    st.dataframe(df.describe().T, use_container_width=True)

    st.subheader("Distribución de variables")
    col_target = st.selectbox("Selecciona columna para analizar:", df.columns)

    conteo = df[col_target].value_counts().reset_index()
    conteo.columns = [col_target, 'Cantidad']

    # Visualización combinada
    c1, c2 = st.columns([2, 1])
    with c1:
        st.bar_chart(conteo.set_index(col_target))
    with c2:
        # Métricas de conteo en formato DF
        st.dataframe(conteo, use_container_width=True, hide_index=True)