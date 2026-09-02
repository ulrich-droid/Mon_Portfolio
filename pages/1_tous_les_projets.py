import streamlit as st
from collections import defaultdict

from src.data.content import get_projects
from src.ui.styles import get_custom_css

st.set_page_config(page_title="Tous les projets", layout="wide")
st.markdown(get_custom_css(), unsafe_allow_html=True)

projects = get_projects()

st.markdown('<div class="section-title">Projets 2025</div>', unsafe_allow_html=True)

archive = defaultdict(lambda: defaultdict(list))
for project in projects:
    archive[project["year"]][project["month"]].append(project)

selected_year = st.selectbox(
    "Choisir l'année",
    options=sorted(archive.keys(), reverse=True),
    index=0,
    key="selected_project_year",
)

st.markdown(
    f"""
    <div class="year-panel">
        <div class="year-label">{selected_year}</div>
    </div>
    """,
    unsafe_allow_html=True,
)

for month in sorted(
    archive[selected_year].keys(),
    key=lambda m: [
        "Janvier", "Février", "Mars", "Avril", "Mai", "Juin",
        "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"
    ].index(m),
):
    st.markdown(f'<div class="month-label">{month}</div>', unsafe_allow_html=True)
    for project in archive[selected_year][month]:
        st.markdown(
            f"""
            <div class="archive-item">
                <div>
                    <a href="{project['link']}" target="_blank">{project['title']}</a>
                </div>
                <span class="archive-date">{month} {selected_year}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

if st.button("Retour à l'accueil", use_container_width=False):
    st.switch_page("app.py")
