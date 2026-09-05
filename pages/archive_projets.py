import streamlit as st

from src.data.content import get_projects
from src.ui.styles import get_custom_css

st.set_page_config(
    page_title="Archive des projets",
    layout="wide",
    initial_sidebar_state="collapsed",
)
st.markdown(get_custom_css(), unsafe_allow_html=True)

projects = get_projects()
archive_years = sorted({project["year"] for project in projects}, reverse=True)
selected_year = st.selectbox("Choisir l'année", archive_years, index=0, key="archive_year")

st.markdown('<div class="section-title">Archive des projets</div>', unsafe_allow_html=True)
st.markdown(f'<div class="year-panel"><div class="year-label">{selected_year}</div></div>', unsafe_allow_html=True)

by_month = {}
for project in projects:
    if project["year"] == selected_year:
        by_month.setdefault(project["month"], []).append(project)

order = [
    "Janvier", "Février", "Mars", "Avril", "Mai", "Juin",
    "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"
]

for month in order:
    if month not in by_month:
        continue
    st.markdown(f'<div class="month-label">{month}</div>', unsafe_allow_html=True)
    for project in by_month[month]:
        st.markdown(
            f"""
            <div class="archive-item">
                <div>
                    <a href="{project['link']}">{project['title']}</a>
                </div>
                <span class="archive-date">{month} {selected_year}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

if st.button("Retour à l'accueil"):
    st.switch_page("home.py")
