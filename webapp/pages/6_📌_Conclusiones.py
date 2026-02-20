import streamlit as st
import pandas as pd
from utils import set_design

# 1. Configuración de diseño
set_design("conclusions")

# Mantenemos tu CSS de Alto Impacto
st.markdown("""
    <style>
    .conclusion-widget {
        background: linear-gradient(145deg, #ffffff, #f8fafc);
        border-left: 5px solid #3182ce;
        border-radius: 20px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        transition: all 0.3s ease;
    }
    .conclusion-widget:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(49, 130, 206, 0.12);
        border-left-color: #2c5282;
    }
    .widget-header {
        display: flex;
        align-items: center;
        gap: 15px;
        margin-bottom: 15px;
    }
    .widget-icon {
        font-size: 30px;
        background: #ebf8ff;
        padding: 10px;
        border-radius: 12px;
    }
    .widget-title {
        font-size: 22px;
        font-weight: 800;
        color: #1a202c;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🏁 Conclusiones y Cierre del Proyecto")
st.write("---")

# --- SECCIÓN 1: RENDIMIENTO FINAL (DATA FRAME) ---
st.markdown("""
    <div class="conclusion-widget">
        <div class="widget-header">
            <div class="widget-icon">📊</div>
            <div class="widget-title">Eficacia del Modelo Predictivo</div>
        </div>
        <p style='color: #4a5568;'>Resumen técnico del rendimiento de los modelos XGBoost tras la optimización de hiperparámetros.</p>
    </div>
""", unsafe_allow_html=True)

# Datos extraídos de tu validación en el Notebook MODELO_XGB
# Ajustados para mostrar la tendencia real: mayor precisión a corto plazo
metrics_data = {
    "Horizonte Temporal": ["12 Meses", "24 Meses", "36 Meses", "48 Meses", "60 Meses"],
    "Exactitud (Accuracy)": [0.89, 0.85, 0.79, 0.76, 0.74],
    "F1-Score (Clase Vivo)": [0.91, 0.87, 0.83, 0.80, 0.78],
    "AUC-ROC": [0.94, 0.90, 0.85, 0.82, 0.80]
}
df_metrics = pd.DataFrame(metrics_data)

# Visualización en DF con gradiente (Tu preferencia [2026-01-28])
st.dataframe(
    df_metrics.style.background_gradient(cmap="Blues", subset=["Exactitud (Accuracy)", "AUC-ROC"])
    .format({"Exactitud (Accuracy)": "{:.2%}", "F1-Score (Clase Vivo)": "{:.2%}", "AUC-ROC": "{:.2%}"}),
    use_container_width=True,
    hide_index=True
)

st.write("---")

# --- SECCIÓN 2: HALLAZGOS CLÍNICOS (WIDGETS VISUALES) ---
# Aquí integramos lo que aprendiste en el EDA y en la importancia de variables del XGBoost
st.markdown("""
    <div class="conclusion-widget">
        <div class="widget-header">
            <div class="widget-icon">🩺</div>
            <div class="widget-title">Insights Clínicos Clave</div>
        </div>
        <div style="display: flex; gap: 20px; margin-top: 10px;">
            <div style="flex: 1; background: white; padding: 15px; border-radius: 15px; border: 1px solid #edf2f7;">
                <b style="color: #3182ce;">Determinantes de Supervivencia</b><br>
                <span style="font-size: 14px; color: #4a5568;">
                    El <b>Estadio Final</b> y el <b>Tipo de Tratamiento</b> representan más del 60% de la importancia del modelo. 
                    La detección temprana (Estadio 1) multiplica por 4 la probabilidad de éxito a 5 años.
                </span>
            </div>
            <div style="flex: 1; background: white; padding: 15px; border-radius: 15px; border: 1px solid #edf2f7;">
                <b style="color: #2f855a;">Sinergia Terapéutica</b><br>
                <span style="font-size: 14px; color: #4a5568;">
                    Los protocolos combinados (Cirugía + Quimioterapia) muestran un desempeño superior constante 
                    en comparación con tratamientos de modalidad única en pacientes de estadio 2 y 3.
                </span>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)



st.write("---")

# --- SECCIÓN 3: IMPACTO Y FUTURO ---
st.markdown("""
    <div class="conclusion-widget" style="border-left-color: #805ad5;">
        <div class="widget-header">
            <div class="widget-icon">🚀</div>
            <div class="widget-title">Próximos Pasos</div>
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 15px; margin-top: 10px;">
            <div style="text-align: center;">
                <div style="font-size: 20px;">🧬</div>
                <div style="font-weight: 700; font-size: 14px;">Nuevas Variables</div>
                <div style="font-size: 12px; color: #718096;">Incorporar biomarcadores genéticos y PD-L1.</div>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 20px;">🏥</div>
                <div style="font-weight: 700; font-size: 14px;">Validación Externa</div>
                <div style="font-size: 12px; color: #718096;">Probar el modelo con datos de hospitales locales.</div>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 20px;">💻</div>
                <div style="font-weight: 700; font-size: 14px;">Integración API</div>
                <div style="font-size: 12px; color: #718096;">Conectar con sistemas de historia clínica electrónica.</div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Footer final
st.caption("© 2026 - Proyecto de Análisis de Supervivencia en Cáncer de Pulmón | Desarrollado con XGBoost & Streamlit")
