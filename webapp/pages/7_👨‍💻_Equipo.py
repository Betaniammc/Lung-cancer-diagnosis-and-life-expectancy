import streamlit as st
import base64
import os
from utils import set_design

# 1. Configuración de página
st.set_page_config(page_title="Equipo", layout="wide")
set_design("equipo")

def get_base64(bin_file):
    """Convierte la imagen a base64 usando una ruta absoluta para evitar errores en la nube."""
    # Obtenemos la raíz del proyecto (subiendo un nivel desde /pages)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    full_path = os.path.join(BASE_DIR, bin_file)
    
    if os.path.exists(full_path):
        with open(full_path, 'rb') as f:
            data = f.read()
        return f"data:image/jpeg;base64,{base64.b64encode(data).decode()}"
    return "" # Retorna vacío si no existe

# --- CSS DE ALTO IMPACTO (Mantenemos tu estilo) ---
st.markdown("""
    <style>
    .team-widget {
        display: flex;
        align-items: center;
        background: linear-gradient(145deg, #ffffff, #f8fafc);
        border-left: 5px solid #3182ce;
        border-radius: 20px;
        padding: 25px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    .widget-img {
        width: 130px;
        height: 130px;
        border-radius: 50%;
        object-fit: cover;
        margin-right: 30px;
        border: 4px solid white;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    .widget-name { font-size: 24px; font-weight: 800; color: #1a202c; }
    .widget-role {
        display: inline-block;
        padding: 4px 12px;
        background: #ebf8ff;
        color: #3182ce;
        border-radius: 50px;
        text-transform: uppercase;
        font-size: 13px;
    }
    .widget-links a {
        text-decoration: none;
        background: white;
        padding: 8px 16px;
        border-radius: 10px;
        font-size: 14px;
        color: #4a5568;
        border: 1px solid #e2e8f0;
        margin-right: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🚀 Equipo de Desarrollo")

def team_widget(nombre, rol, path_foto, linkedin, github):
    img_base64 = get_base64(path_foto)
    
    # Si no encuentra la imagen, mostramos un placeholder circular con la inicial
    if not img_base64:
        img_html = f'<div class="widget-img" style="display:flex;align-items:center;justify-content:center;background:#cbd5e0;font-size:40px;font-weight:bold;color:white;">{nombre[0]}</div>'
    else:
        img_html = f'<img src="{img_base64}" class="widget-img">'

    st.markdown(f"""
        <div class="team-widget">
            {img_html}
            <div class="widget-info">
                <div class="widget-name">{nombre}</div>
                <div class="widget-role">{rol}</div>
                <div class="widget-links" style="margin-top:15px;">
                    <a href="{linkedin}" target="_blank">🔗 LinkedIn</a>
                    <a href="{github}" target="_blank">💻 GitHub</a>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# 2. Listado de integrantes (Usa la ruta relativa desde la raíz del proyecto)
team_widget("Betania Medina", "Data Scientist", "assets/betania.jpg",
            "https://linkedin.com/in/betania-medina-b2b733269/", "https://github.com/Betaniammc")

team_widget("Carlos Restrepo", "Data Scientist", "assets/carlos.jpg",
            "https://www.linkedin.com/in/carlos-restrepo-a7b188390/", "https://github.com/carlos-villa-restrepo")

team_widget("Elius Trujillo", "Data Scientist", "assets/elius.jpg",
            "https://www.linkedin.com/in/elius-trujillo", "https://github.com/elius123ef")