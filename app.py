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


st.markdown('<div class="topline"><span>MF / BI · Marketing Analytics</span><span>Olavarría, AR · Disponible para proyectos</span></div>', unsafe_allow_html=True)
hero_title, hero_note = st.columns([1.45, 1], gap="large")
with hero_title:
    st.markdown('<h1 class="hero-title">De datos complejos a decisiones que importan.</h1>', unsafe_allow_html=True)
with hero_note:
    st.markdown('<div class="hero-note">Hago que los datos complejos se vuelvan accionables.<br><span style="font-weight:400;color:#64716d">Conecto análisis, contexto y decisiones de negocio.</span></div>', unsafe_allow_html=True)
st.markdown(
    '<p class="hero-copy">Soy Matías Fuentes, analista de datos especializado en Business Intelligence y Marketing Analytics. Conecto SQL, Python y dashboards para transformar datos crudos en métricas accionables de rentabilidad, conversión y retención.</p>',
    unsafe_allow_html=True,
)
st.link_button("Explorar proyectos ↓", "#proyectos", use_container_width=False)

st.markdown(
    '<div class="stats"><div><span class="stat-number">144K+</span><span class="stat-label">respuestas analizadas</span></div><div><span class="stat-number">$1.39M</span><span class="stat-label">en pérdidas detectadas</span></div><div><span class="stat-number">500K+</span><span class="stat-label">transacciones modeladas</span></div><div><span class="stat-number">80%</span><span class="stat-label">del churn en el mes 1</span></div></div>',
    unsafe_allow_html=True,
)

st.markdown('<div id="proyectos"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-head"><div><div class="eyebrow">TRABAJO SELECCIONADO</div><h2>Casos con una pregunta<br>de negocio detrás.</h2></div></div>', unsafe_allow_html=True)

categories = ["Todos", "BI", "Data Science", "Marketing"]
selected_category = st.radio("Filtrar por disciplina", categories, horizontal=True, label_visibility="collapsed")
filtered_projects = [project for project in PROJECTS if selected_category == "Todos" or project["categoria"] == selected_category]

if filtered_projects and selected_category in ("Todos", "Data Science"):
    render_project(filtered_projects[0], featured=True)
    st.markdown("<br>", unsafe_allow_html=True)
    filtered_projects = filtered_projects[1:]

project_columns = st.columns(2, gap="large")
for index, project in enumerate(filtered_projects):
    with project_columns[index % 2]:
        render_project(project)
    if index % 2 == 1 and index < len(filtered_projects) - 1:
        st.markdown("<br>", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown('<div class="eyebrow">HABLEMOS</div><h2>¿Tenés un problema<br>de datos?</h2>', unsafe_allow_html=True)
st.markdown('<p class="hero-copy">Estoy abierto a oportunidades en BI, Marketing Analytics y Data Science. Un buen proyecto empieza con una buena pregunta.</p>', unsafe_allow_html=True)
contact_columns = st.columns(3)
with contact_columns[0]:
    st.link_button("LinkedIn", "https://www.linkedin.com/in/matiasfuentes1/", use_container_width=True)
with contact_columns[1]:
    st.link_button("GitHub", "https://github.com/Matias-Fuentes1", use_container_width=True)
with contact_columns[2]:
    st.link_button("Enviar email", "mailto:matifuentes742@gmail.com", use_container_width=True)

