import streamlit as st
from pathlib import Path
from projects import PROJECTS

# Configuración de entorno y metadatos de la plataforma
st.set_page_config(
    page_title="Matías Fuentes | Consultoría de Datos e Insights",
    page_icon="📊",
    layout="wide",
)

# 🛠️ 1. DEFINICIÓN DE LA FUNCIÓN PARA LAS BADGES (Insertada al inicio)
def render_stack_badges(stack: list[str]):
    badges_html = " ".join(
        f'<span style="display: inline-block; background-color:#1e293b; color:#e2e8f0; '
        f'padding:4px 12px; border-radius:12px; font-size:0.8rem; margin-right:6px; '
        f'margin-bottom:6px; font-family: monospace;">{tool}</span>'
        for tool in stack
    )
    # Metemos un envoltorio div para controlar el espaciado vertical
    st.markdown(f'<div style="margin-top: 8px; margin-bottom: 12px;">{badges_html}</div>', unsafe_allow_html=True)


# Sección de encabezado: Posicionamiento profesional y contacto directo
st.title("Matías Fuentes")
st.markdown("#### Analista de Datos · Business Intelligence & Marketing Analytics")
st.caption("SQL · Power BI · BigQuery · Python · Looker Studio · GA4")

st.markdown("""
<style>
    div[data-testid="stImage"] img {
        max-height: 280px;
        object-fit: cover;
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.link_button("💼 LinkedIn", "https://www.linkedin.com/in/matiasfuentes1/")
with col2:
    st.link_button("💻 GitHub", "https://github.com/Matias-Fuentes1")
with col3:
    st.link_button("✉️ Email", "mailto:matifuentes742@gmail.com")

st.divider()

# Renderizado de proyectos: Jerarquía de información basada en la Respuesta Primero (Minto Pyramid)
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
            
            # 🛠️ 2. REEMPLAZO DEL ST.CAPTION POR LAS BADGES INTERACTIVAS
            render_stack_badges(proyecto["stack"])

            # Acceso a repositorios de auditoría y reportes de alta resolución
            btn_col1, btn_col2 = st.columns(2)
            with btn_col1:
                if proyecto["github_url"]:
                    st.link_button("Ver Auditoría en GitHub", proyecto["github_url"], use_container_width=True)
            with btn_col2:
                if proyecto["dashboard_url"]:
                    st.link_button("Ver Dashboard", proyecto["dashboard_url"], use_container_width=True)
