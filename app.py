import base64
import streamlit as st
from pathlib import Path
from projects import PROJECTS


st.set_page_config(
    page_title="Matías Fuentes | BI + Marketing Analytics",
    page_icon="MF",
    layout="wide",
    initial_sidebar_state="collapsed",
)


def render_stack_badges(stack: list[str]) -> None:
    badges = "".join(f'<span class="badge">{tool}</span>' for tool in stack)
    st.markdown(f'<div class="badges">{badges}</div>', unsafe_allow_html=True)


def render_project(project: dict, featured: bool = False) -> None:
    image_path = Path(__file__).parent / project["imagen"]
    if featured:
        st.markdown('<div class="eyebrow">CASO DESTACADO / 01</div>', unsafe_allow_html=True)
        left, right = st.columns([1.15, 1], gap="large")
        with left:
            if image_path.exists():
                st.image(str(image_path), use_container_width=True)
        with right:
            st.markdown(f'<div class="project-type">{project["categoria"]} · DATA STORY</div>', unsafe_allow_html=True)
            st.markdown(f'<h2>{project["titulo"]}</h2>', unsafe_allow_html=True)
            st.markdown(f'<p class="finding">{project["hallazgo_clave"]}</p>', unsafe_allow_html=True)
            st.write(project["resumen"])
            render_stack_badges(project["stack"])
            buttons = st.columns(2)
            with buttons[0]:
                if project["github_url"]:
                    st.link_button("GitHub", project["github_url"], use_container_width=True)
            with buttons[1]:
                if project["dashboard_url"]:
                    st.link_button("Dashboard", project["dashboard_url"], use_container_width=True)
        return

    with st.container(border=True):
        st.markdown(f'<div class="project-type">{project["categoria"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<h3>{project["titulo"]}</h3>', unsafe_allow_html=True)
        if image_path.exists():
            st.image(str(image_path), use_container_width=True)
        st.markdown(f'<p class="finding">{project["hallazgo_clave"]}</p>', unsafe_allow_html=True)
        st.write(project["resumen"])
        render_stack_badges(project["stack"])
        actions = st.columns(2)
        with actions[0]:
            if project["github_url"]:
                st.link_button("GitHub", project["github_url"], use_container_width=True)
        with actions[1]:
            if project["dashboard_url"]:
                st.link_button("Dashboard", project["dashboard_url"], use_container_width=True)


styles_path = Path(__file__).parent / "styles.css"
st.markdown(f"<style>{styles_path.read_text()}</style>", unsafe_allow_html=True)


photo_path = Path(__file__).parent / "foto.jpg"
photo_data = base64.b64encode(photo_path.read_bytes()).decode() if photo_path.exists() else ""
brand_mark = f'<img src="data:image/jpeg;base64,{photo_data}" alt="" />' if photo_data else "MF"

# Rutas de los CVs apuntando a assets
cv_marketing_path = Path(__file__).parent / "assets" / "Fuentes_Matias_cv.pdf"
cv_bi_path = Path(__file__).parent / "assets" / "Matias_Fuentes_cv.pdf"

header_columns = st.columns([2.8, 7.2], gap="small")
with header_columns[0]:
    st.markdown(
        f'<a class="brand" href="#inicio"><span class="brand-mark">{brand_mark}</span><span><strong>Matías Fuentes</strong><small>BI &amp; Marketing Analytics</small></span></a>',
        unsafe_allow_html=True,
    )
with header_columns[1]:
    navigation_columns = st.columns([7.1, 2.9], gap="small")
    with navigation_columns[0]:
        st.markdown(
            '<nav class="site-nav"><div class="nav-links"><a href="#inicio">Inicio</a><a href="#sobre-mi">Sobre mí</a><a href="#experiencia">Experiencia</a><a href="#proyectos">Casos de éxito</a><a href="#contacto">Contacto</a></div></nav>',
            unsafe_allow_html=True,
        )
    with navigation_columns[1]:
        cv_columns = st.columns(2, gap="small")
        with cv_columns[0]:
            if cv_marketing_path.exists():
                st.download_button("CV Marketing", cv_marketing_path.read_bytes(), file_name="Matias_Fuentes_CV_Marketing_Analytics.pdf", mime="application/pdf", use_container_width=True)
        with cv_columns[1]:
            if cv_bi_path.exists():
                st.download_button("CV BI", cv_bi_path.read_bytes(), file_name="Matias_Fuentes_CV_Business_Intelligence.pdf", mime="application/pdf", use_container_width=True)

st.markdown('<div id="inicio" class="topline"><span>Olavarría, AR · Disponible para proyectos</span></div>', unsafe_allow_html=True)
hero_title, hero_note = st.columns([1.45, 1], gap="large")
with hero_title:
    st.markdown('<h1 class="hero-title">De datos complejos a decisiones que importan.</h1>', unsafe_allow_html=True)
    st.markdown(
        '<p class="hero-copy">Soy Matías Fuentes, analista de datos especializado en Business Intelligence y Marketing Analytics. Conecto SQL, Python y dashboards para transformar datos crudos en métricas accionables de rentabilidad, conversión y retención.</p>',
        unsafe_allow_html=True,
    )
    st.markdown('<a class="project-cta" href="#proyectos">Explorar proyectos ↓</a>', unsafe_allow_html=True)
with hero_note:
    st.markdown('<div class="metric-panel"><div class="metric-panel-heading"><span>Áreas de análisis</span><b>● Disponible para nuevas oportunidades</b></div><h3>Del diagnóstico a la acción</h3><div class="focus-grid"><div class="focus-card"><span>▥ Business Intelligence</span><strong>KPIs · Dashboards</strong><div class="chart-bars"><i></i><i></i><i></i><i></i><i></i></div></div><div class="focus-card"><span>⌁ Marketing</span><strong>Funnel Analytics</strong><div class="chart-funnel"><i></i><i></i><i></i><i></i></div></div><div class="focus-card"><span>♧ Clientes</span><strong>Cohort Analysis</strong><div class="chart-grid"><i></i><i></i><i></i><i></i><i></i><i></i></div></div><div class="focus-card"><span>◌ Data Science</span><strong>Predictive Models</strong><div class="chart-line"><i></i><i></i><i></i><i></i><i></i></div></div></div></div>', unsafe_allow_html=True)

st.markdown(
    '<div class="stats"><div><span class="stat-icon">▥</span><span class="stat-number">144K+</span><span class="stat-label">respuestas analizadas</span></div><div><span class="stat-icon">$</span><span class="stat-number">$1.39M</span><span class="stat-label">en pérdidas detectadas</span></div><div><span class="stat-icon">⇄</span><span class="stat-number">500K+</span><span class="stat-label">transacciones modeladas</span></div><div><span class="stat-icon">↘</span><span class="stat-number">80%</span><span class="stat-label">del churn en el mes 1</span></div></div>',
    unsafe_allow_html=True,
)

st.markdown('<div id="sobre-mi" class="profile-section"><div class="section-head"><div><div class="eyebrow">SOBRE MÍ</div><h2>Más de 2 años formándome en datos y negocio.</h2></div></div></div>', unsafe_allow_html=True)
st.markdown('<p class="profile-lead">Hoy mi foco no es solo entender qué está pasando con los datos, sino también comprender el porqué conductual que hay detrás de los números.</p>', unsafe_allow_html=True)
st.markdown('<p class="hero-copy">Ese enfoque atraviesa mi trabajo: combino análisis, visualización y contexto de negocio para detectar patrones, explicar comportamientos y convertir los hallazgos en decisiones concretas.</p>', unsafe_allow_html=True)

st.markdown('<div id="experiencia" class="section-head experience-head"><div><div class="eyebrow">EXPERIENCIA</div><h2>Cómo trabajo con los datos.</h2></div></div>', unsafe_allow_html=True)
experience_columns = st.columns(2, gap="large")
experiences = [
    ("Business Intelligence", "Modelado de datos, definición de KPIs y dashboards ejecutivos para analizar rentabilidad, retención y performance."),
    ("Marketing Analytics", "Funnel de conversión, adquisición y cohortes para entender el comportamiento de clientes y oportunidades de crecimiento."),
]
for column, (title, description) in zip(experience_columns, experiences):
    with column:
        st.markdown(f'<article class="experience-item"><h3>{title}</h3><p>{description}</p></article>', unsafe_allow_html=True)

st.markdown('<div id="proyectos"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-head"><div><div class="eyebrow">CASOS DE ÉXITO</div><h2>Casos con una pregunta<br>de negocio detrás.</h2></div></div>', unsafe_allow_html=True)

categories = ["Todos", "BI", "Data Science", "Marketing"]
selected_category = st.radio("Filtrar por disciplina", categories, horizontal=True, label_visibility="collapsed")
filtered_projects = [project for project in PROJECTS if selected_category == "Todos" or project["categoria"] == selected_category]

if filtered_projects and selected_category == "Todos":
    featured_project = next((project for project in filtered_projects if project["dashboard_url"]), filtered_projects[0])
    render_project(featured_project, featured=True)
    st.markdown("<br>", unsafe_allow_html=True)
    filtered_projects = [project for project in filtered_projects if project is not featured_project]

project_columns = st.columns(2, gap="large")
for index, project in enumerate(filtered_projects):
    with project_columns[index % 2]:
        render_project(project)
    if index % 2 == 1 and index < len(filtered_projects) - 1:
        st.markdown("<br>", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown('<div id="contacto" class="contact-heading"><div class="eyebrow">HABLEMOS</div><h2>¿Charlamos?</h2></div>', unsafe_allow_html=True)
st.markdown('<p class="hero-copy contact-copy">Estoy disponible para sumarme a proyectos de Business Intelligence, Marketing Analytics y análisis de datos — desde armar el dashboard hasta entender qué hay detrás del número.</p>', unsafe_allow_html=True)

contact_columns = st.columns(3)
with contact_columns[0]:
    st.link_button("LinkedIn", "https://www.linkedin.com/in/matiasfuentes1/", use_container_width=True)
with contact_columns[1]:
    st.link_button("GitHub", "https://github.com/Matias-Fuentes1", use_container_width=True)
with contact_columns[2]:
    st.link_button("Enviar email", "mailto:matifuentes742@gmail.com", use_container_width=True)
