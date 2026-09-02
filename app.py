import streamlit as st

from src.data.content import get_contact, get_cv_bytes, get_cv_filename, get_profile, get_projects, get_recent_projects, get_skills
from src.ui.components import render_contact, render_footer, render_hero, render_projects, render_skills
from src.ui.styles import get_custom_css

st.set_page_config(
    page_title="Portfolio | IA & Big Data",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(get_custom_css(), unsafe_allow_html=True)

profile = get_profile()
skills = get_skills()
projects = get_projects()
recent_projects = get_recent_projects()
contact = get_contact()
cv_data = get_cv_bytes()
cv_file_name = get_cv_filename()

render_hero(profile, cv_data, cv_file_name)
render_skills(skills)
render_projects(projects, recent_projects)
render_contact(contact)
render_footer()
