import streamlit as st
from pathlib import Path
from projects import PROJECTS

# Configuración de entorno y metadatos de la plataforma
st.set_page_config(
    page_title="Matías Fuentes | Consultoría de Datos e Insights",
    page_icon="📊",
    layout="wide",
)

# Seccion de encabezado: Posicionamiento profesional y contacto directo
st.title("Matías Fuentes")
st.subheader("Data-Driven Strategy & Behavioral Insights") # Título más agresivo

st.markdown("""
**Auditoría de Microdatos | Optimización de Rentabilidad | Arquitectura de Decisión.**
Portfolio de proyectos estratégicos enfocados en detectar fugas de capital, ineficiencias estructurales 
y patrones de comportamiento financiero.
""")

col1, col2, col3 = st.columns(3)
with col1:
    st.link_button("💼 LinkedIn", "https://www.linkedin.com/in/matiasfuentes1/")
with col2:
    st.link_button("💻 GitHub", "https://github.com/Matias-Fuentes1")
with col3:
    st.link_button("✉️ Email", "mailto:matifuentes742@gmail.com")

st.divider()

# Renderizado de proyectos: Jerarquía de información basada en la Respuesta Primero (Minto Pyramid)
# Se prioriza el hallazgo de negocio y la evidencia visual antes que el contexto metodológico.
cols = st.columns(2)

for i, proyecto in enumerate(PROJECTS):
    with cols[i % 2]:
        with st.container(border=True):
            # Título y conclusión estratégica (Impacto de Negocio)
            st.markdown(f"### {proyecto['titulo']}")
            st.markdown(f"**Hallazgo clave:** {proyecto['hallazgo_clave']}")

            # Validación estadística y visual (Evidencia técnica)
            imagen_path = Path(proyecto["imagen"])
            if imagen_path.exists():
                st.image(str(imagen_path), use_container_width=True)
            else:
                st.info(f"📷 Evidencia técnica: `{proyecto['imagen']}` (Cargando...)")

            # Metodología, alcance y stack tecnológico (Contexto)
            st.write(proyecto["resumen"])
            st.caption(f"**Stack Técnico:** {' · '.join(proyecto['stack'])}")

            # Acceso a repositorios de auditoría y reportes de alta resolución
            btn_col1, btn_col2 = st.columns(2)
            with btn_col1:
                if proyecto["github_url"]:
                    st.link_button("Ver Auditoría en GitHub", proyecto["github_url"], use_container_width=True)
            with btn_col2:
                if proyecto["dashboard_url"]:
                    st.link_button("Ver Dashboard", proyecto["dashboard_url"], use_container_width=True)
