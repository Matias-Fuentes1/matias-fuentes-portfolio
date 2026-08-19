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
    image_path = Path(project["imagen"])
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
                    st.link_button("Ver análisis", project["github_url"], use_container_width=True)
            with buttons[1]:
                if project["dashboard_url"]:
                    st.link_button("Abrir dashboard", project["dashboard_url"], use_container_width=True)
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


st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Manrope:wght@400;500;600;700;800&display=swap');
    :root { --ink:#172321; --muted:#64716d; --paper:#f4f1ea; --lime:#c9ee65; --coral:#f47c63; --line:#d7d8cd; }
    .stApp { background:var(--paper); color:var(--ink); }
    [data-testid="stHeader"] { background:transparent; }
    [data-testid="stToolbar"] { visibility:hidden; }
    .block-container { max-width:1280px; padding:4.5rem 2.4rem 5rem; }
    html, body, [class*="css"] { font-family:'Manrope', sans-serif; }
    h1, h2, h3 { color:var(--ink); letter-spacing:-.04em; font-weight:800; }
    h1 { font-size:clamp(3.2rem, 6vw, 6.2rem); line-height:.95; margin:1rem 0 1.5rem; }
    .hero-title { white-space:nowrap; }
    h2 { font-size:clamp(2rem, 4vw, 3.4rem); line-height:1; margin:.4rem 0 1rem; }
    h3 { font-size:1.55rem; line-height:1.08; margin:.5rem 0 1rem; }
    p, .stMarkdown, .stCaption { color:var(--muted); }
    .topline { display:flex; justify-content:space-between; border-bottom:1px solid var(--line); padding-bottom:1rem; color:var(--ink); font-family:'DM Mono', monospace; font-size:.72rem; text-transform:uppercase; letter-spacing:.08em; }
    .hero-copy { max-width:760px; font-size:1.16rem; line-height:1.6; margin-bottom:2rem; }
    .eyebrow, .project-type { color:#607f2c; font-family:'DM Mono', monospace; font-size:.72rem; font-weight:500; letter-spacing:.1em; text-transform:uppercase; }
    .hero-note { border-left:5px solid var(--coral); padding:1rem 1.2rem; background:#fffdf8; font-weight:600; max-width:460px; }
    .stats { display:flex; gap:3rem; border-top:1px solid var(--line); border-bottom:1px solid var(--line); padding:1.25rem 0; margin:3.5rem 0 5rem; }
    .stat-number { display:block; color:var(--ink); font-size:2rem; font-weight:800; letter-spacing:-.05em; }
    .stat-label { color:var(--muted); font-family:'DM Mono', monospace; font-size:.68rem; text-transform:uppercase; }
    .section-head { display:flex; justify-content:space-between; align-items:end; margin-bottom:1.5rem; }
    .section-head h2 { margin:0; }
    .finding { color:var(--ink) !important; font-size:1.02rem; font-weight:700; line-height:1.45; }
    .badges { margin:1.1rem 0 1.3rem; }
    .badge { display:inline-block; background:var(--ink); color:#eff3df; padding:.35rem .65rem; margin:0 .35rem .35rem 0; border-radius:999px; font-family:'DM Mono', monospace; font-size:.68rem; }
    div[data-testid="stImage"] img { max-height:390px; object-fit:cover; border-radius:2px; }
    div[data-testid="stVerticalBlockBorderWrapper"] { background:#fffdf8; border:1px solid var(--line); border-radius:2px; padding:1.4rem; height:100%; }
    .stButton > button, .stLinkButton > a { border-radius:2px !important; font-weight:700 !important; }
    .stLinkButton > a { background:var(--ink); color:#fffdf8; border-color:var(--ink); }
    @media (max-width: 700px) { .block-container { padding:3.5rem 1.2rem 3rem; } .hero-title { white-space:normal; } .topline { font-size:.62rem; gap:1rem; } .topline span:last-child { text-align:right; } .stats { gap:1.2rem; margin:2.5rem 0 3rem; } .stat-number { font-size:1.45rem; } .stat-label { font-size:.56rem; } .section-head { display:block; } }
    </style>
    """,
    unsafe_allow_html=True,
)


st.markdown('<div class="topline"><span>MF / BI + Marketing Analytics</span><span>Olavarría, AR · Disponible para proyectos</span></div>', unsafe_allow_html=True)
st.markdown('<h1 class="hero-title">Datos claros para decisiones difíciles.</h1>', unsafe_allow_html=True)
st.markdown(
    '<p class="hero-copy">Soy Matías Fuentes, analista de datos especializado en Business Intelligence y Marketing Analytics. Conecto SQL, Python y dashboards para transformar datos crudos en métricas accionables de rentabilidad, conversión y retención.</p>',
    unsafe_allow_html=True,
)
hero_left, hero_right = st.columns([1.5, 1], gap="large")
with hero_left:
    st.link_button("Explorar proyectos ↓", "#proyectos", use_container_width=False)
with hero_right:
    st.markdown('<div class="hero-note">Del dato crudo a la decisión.<br><span style="font-weight:400;color:#64716d">La herramienta es el medio; el impacto es el resultado.</span></div>', unsafe_allow_html=True)

st.markdown(
    '<div class="stats"><div><span class="stat-number">144K+</span><span class="stat-label">respuestas analizadas</span></div><div><span class="stat-number">$1.39M</span><span class="stat-label">en pérdidas detectadas</span></div><div><span class="stat-number">500K+</span><span class="stat-label">transacciones modeladas</span></div><div><span class="stat-number">80%</span><span class="stat-label">del churn en los primeros 30 días</span></div></div>',
    unsafe_allow_html=True,
)

st.markdown('<div id="proyectos"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-head"><div><div class="eyebrow">TRABAJO SELECCIONADO</div><h2>Casos con una pregunta<br>de negocio detrás.</h2></div></div>', unsafe_allow_html=True)

categories = ["Todos"] + sorted({project["categoria"] for project in PROJECTS})
selected_category = st.radio("Filtrar por disciplina", categories, horizontal=True, label_visibility="collapsed")
filtered_projects = [project for project in PROJECTS if selected_category == "Todos" or project["categoria"] == selected_category]

if selected_category == "Todos" and filtered_projects:
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
