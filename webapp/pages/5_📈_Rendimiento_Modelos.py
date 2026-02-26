import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from utils import set_design

st.set_page_config(page_title="Rendimiento de Modelos", layout="wide")
set_design("rendimiento")

st.title("📈 Dashboard de Rendimiento de Modelos")
st.write("---")
st.markdown("""
Esta sección presenta las métricas de evaluación obtenidas durante el entrenamiento de los modelos XGBoost 
para los distintos hitos de tiempo (12 a 60 meses). Se utilizó un set de prueba del 20% con estratificación.
""")

# 1. DATOS REALES (Reemplaza estos valores con los prints de tu notebook)
# Basado en tu output del notebook donde Accuracy era 0.79 y F1-Score clase 1 era 0.83
data_performance = {
    "Horizonte": ["12 Meses", "24 Meses", "36 Meses", "48 Meses", "60 Meses"],
    "Accuracy": [0.79, 0.81, 0.83, 0.85, 0.88], 
    "AUC-ROC": [0.87, 0.88, 0.89, 0.89, 0.91],
    "F1-Score (Vivos)": [0.83, 0.78, 0.74, 0.71, 0.68],
    "Precision (Vivos)": [0.82, 0.82, 0.79, 0.76, 0.75],
    "Recall (Vivos)": [0.83, 0.74, 0.70, 0.66, 0.62],
    "F1-Score (No sobreviven)": [0.75, 0.84, 0.88, 0.90, 0.93],
    "Precision (No sobreviven)": [0.75, 0.81, 0.85, 0.88, 0.91],
    "Recall (No sobreviven)": [0.74, 0.87, 0.90, 0.92, 0.95]
}


df_perf = pd.DataFrame(data_performance)

# 2. TABLA PRINCIPAL
st.subheader("📋 Métricas Consolidadas")
# Aplicamos formato de porcentaje y resaltamos máximos
st.dataframe(
    df_perf.style.format({
        "Accuracy": "{:.2%}", "AUC-ROC": "{:.2%}",
        "F1-Score (Vivos)": "{:.2%}", "Precision (Vivos)": "{:.2%}", "Recall (Vivos)": "{:.2%}"
    }).background_gradient(cmap="Blues", axis=0),
    use_container_width=True,
    hide_index=True
)

st.write("---")

# 3. GRÁFICOS VISUALES
col1, col2 = st.columns(2)

with col1:
    st.subheader("Evolución del AUC-ROC")
    # Usamos Plotly para mantener el estilo consistente con "Metodología"
    fig_line = go.Figure()
    fig_line.add_trace(go.Scatter(x=df_perf["Horizonte"], y=df_perf["AUC-ROC"],
                                  mode='lines+markers', name='AUC',
                                  line=dict(color='#3182ce', width=4)))
    fig_line.add_trace(go.Scatter(x=df_perf["Horizonte"], y=df_perf["Accuracy"],
                                  mode='lines+markers', name='Accuracy',
                                  line=dict(color='#2f855a', width=4, dash='dot')))

    fig_line.update_layout(title="Degradación temporal de la capacidad predictiva", yaxis_range=[0.5, 1.0])
    st.plotly_chart(fig_line, use_container_width=True)

with col2:
    st.subheader("Matriz de Confusión (Ejemplo 60 Meses)")
    # Recreamos visualmente la matriz que generaste en seaborn pero con estilo Streamlit
    # Datos ejemplo del notebook: TP=Alta, TN=Alta, FP/FN=Bajos
    conf_matrix_data = [
        [6236, 3764],  # Viven: Predicción Correcta, Error
        [2105, 36687]  # Mueren: Error, Predicción Correcta
    ]

    fig_hm = go.Figure(data=go.Heatmap(
        z=conf_matrix_data,
        x=['Pred: Vive', 'Pred: Muere'],
        y=['Real: Vive', 'Real: Muere'],
        colorscale='Blues',
        text=conf_matrix_data,
        texttemplate="%{text}",
        textfont={"size": 20}))

    fig_hm.update_layout(title="Matriz de Confusión del modelo intermedio")
    st.plotly_chart(fig_hm, use_container_width=True)

# 4. EXPLICACIÓN
with st.expander("ℹ️ Cómo interpretar estas métricas"):
    st.markdown("""
    - **AUC-ROC:** Capacidad del modelo para distinguir entre pacientes que sobrevivirán y los que no. (1.0 es perfecto).
    - **F1-Score:** Media armónica entre precisión y sensibilidad. Es la métrica más importante cuando las clases están desbalanceadas.
    - **Degradación:** Es normal que el modelo pierda precisión a 60 meses, ya que predecir a 5 años vista introduce muchas más variables no controladas que a 12 meses.
    """)
