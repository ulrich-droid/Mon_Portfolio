import streamlit as st

from src.services.email_service import send_contact_email


def set_portfolio_view(view):
    st.session_state["portfolio_view"] = view


def render_hero(profile, cv_data=None, cv_file_name="CV.pdf"):
    if "portfolio_view" not in st.session_state:
        st.session_state["portfolio_view"] = "projects"

    text_col, image_col = st.columns([2.4, 1.2], vertical_alignment="top")

    with text_col:
        st.markdown(
            f"""
            <div class="hero-kicker">PORTFOLIO / DATA & IA</div>
            <div class="hero-title">{profile['name']}</div>
            <div class="hero-subtitle">{profile['title']}</div>
            <div class="hero-location">{profile['location']}</div>
            <div class="hero-summary">{profile['summary']}</div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            '''
            <div class="hero-actions">
                <a href="#projets" class="hero-link primary">Voir les projets</a>
                <a href="#archives" class="hero-link secondary">Voir les archives</a>
            </div>
            ''',
            unsafe_allow_html=True,
        )

        if cv_data is not None:
            st.download_button(
                label="Télécharger le CV",
                data=cv_data,
                file_name=cv_file_name,
                mime="application/pdf",
            )

    with image_col:
        st.markdown('<div class="profile-frame">', unsafe_allow_html=True)
        st.image(
            profile["photo_url"],
            width=330,
            use_container_width=False,
        )
        st.markdown('</div>', unsafe_allow_html=True)



def render_skills(skills):
    st.markdown('<div class="section-title">Compétences Techniques</div>', unsafe_allow_html=True)

    skill_items = list(skills.items())
    skill_columns = st.columns(2)

    for index, (category, items) in enumerate(skill_items):
        with skill_columns[index % 2]:
            st.markdown(
                f"""
                <div class="skill-card">
                    <h3>{category}</h3>
                    {''.join(f'<span class="tech-badge">{item}</span>' for item in items)}
                </div>
                """,
                unsafe_allow_html=True,
            )


def render_projects(projects, recent_projects=None):
    if recent_projects is None:
        recent_projects = projects[:4]

    st.markdown('<div id="projets" class="section-title">Projets récents</div>', unsafe_allow_html=True)

    for row_start in range(0, len(recent_projects), 2):
        project_columns = st.columns(2)
        for column, project in zip(project_columns, recent_projects[row_start:row_start + 2]):
            with column:
                project_index = recent_projects.index(project) + 1
                st.markdown(
                    f"""
                    <div class="project-card">
                        <div class="project-index">{project_index:02d}</div>
                        <h3>{project['title']}</h3>
                        <div>
                            {''.join(f'<span class="tech-badge">{item}</span>' for item in project['stack'])}
                        </div>
                        <p>{project['description']}</p>
                        <a href="{project['link']}" class="project-link" target="_blank" rel="noopener noreferrer">
                            Voir le projet sur GitHub <span>&rarr;</span>
                        </a>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

        if row_start + 2 < len(recent_projects):
            st.markdown('<div class="project-row-gap"></div>', unsafe_allow_html=True)

    st.markdown(
        '''
        <div id="archives" class="project-archive">
            <div class="section-title archive-title">Archive des projets</div>
        </div>
        ''',
        unsafe_allow_html=True,
    )

    years = sorted({project["year"] for project in projects}, reverse=True)
    if not years:
        st.warning("Aucun projet disponible pour l'archive.")
        return

    selected_year = st.selectbox("Choisir une année", years, index=0, key="archive_year")

    st.markdown(
        f"""
        <div class="year-panel">
            <div class="year-label">{selected_year}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    months = [
        "Janvier", "Février", "Mars", "Avril", "Mai", "Juin",
        "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"
    ]
    grouped = {month: [] for month in months}
    for project in projects:
        if project["year"] == selected_year:
            grouped.setdefault(project["month"], []).append(project)

    for month in months:
        if not grouped.get(month):
            continue
        st.markdown(f'<div class="month-label">{month}</div>', unsafe_allow_html=True)
        for project in grouped[month]:
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

    st.markdown(
        '<div class="archive-return"><a href="#projets" class="hero-link secondary">Retour aux projets récents</a></div>',
        unsafe_allow_html=True,
    )


def render_contact(contact):
    st.markdown('<div class="section-title">Contact</div>', unsafe_allow_html=True)

    form_col, info_col = st.columns([1.3, 0.9])

    with form_col:
        with st.form("modern_contact_form", clear_on_submit=True):
            st.markdown('<div class="contact-panel">', unsafe_allow_html=True)
            name = st.text_input("Nom complet")
            email = st.text_input("Adresse email")
            message = st.text_area("Votre message", height=160)
            submitted = st.form_submit_button("Envoyer le message", use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

            if submitted:
                if not name.strip() or not email.strip() or not message.strip():
                    st.warning("Veuillez remplir tous les champs avant d'envoyer le message.")
                else:
                    ok, result = send_contact_email(name.strip(), email.strip(), message.strip())
                    if ok:
                        st.success(result)
                    else:
                        st.error(result)

    with info_col:
        st.markdown(
            f"""
            <div class="contact-panel">
                <h3>Réseaux</h3>
                <a href="tel:{contact['phone']}" class="social-link">
                    <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.6 10.8c1.7 3.3 4.5 6.1 7.8 7.8l2.6-2.6c.3-.3.8-.4 1.2-.2 1.3.4 2.8.7 4.3.7.7 0 1.2.5 1.2 1.2V20c0 .7-.5 1.2-1.2 1.2C10.8 21.2 2.8 13.2 2.8 4.2c0-.7.5-1.2 1.2-1.2h3.2c.7 0 1.2.5 1.2 1.2 0 1.5.2 3 .7 4.3.1.4 0 .9-.2 1.2l-2.6 2.6z"/></svg>
                    <span class="social-value">{contact['phone']}</span>
                </a>
                <a href="mailto:{contact['email']}" class="social-link">
                    <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 6.75A2.75 2.75 0 0 1 5.75 4h12.5A2.75 2.75 0 0 1 21 6.75v10.5A2.75 2.75 0 0 1 18.25 20H5.75A2.75 2.75 0 0 1 3 17.25V6.75zm2.2-.75 6.8 5.25 6.8-5.25H5.2zm14.05 2.14-6.16 4.75a1 1 0 0 1-1.18 0L4.75 8.14v9.11c0 .41.34.75.75.75h12.99c.41 0 .75-.34.75-.75V8.14z"/></svg>
                    <span class="social-value">{contact['email']}</span>
                </a>
                <a href="{contact['linkedin']}" target="_blank" class="social-link">
                    <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.94 8.5A1.5 1.5 0 1 1 6.94 5a1.5 1.5 0 0 1 0 3.5zM5.5 9.75h2.88v8.75H5.5V9.75zm4.78 0h2.76v1.2h.04c.38-.72 1.32-1.48 2.72-1.48 2.92 0 3.46 1.92 3.46 4.42v4.61h-2.88v-4.32c0-1.03-.02-2.35-1.43-2.35-1.43 0-1.65 1.12-1.65 2.27v4.4H10.28V9.75z"/></svg>
                    <span class="social-value">LinkedIn</span>
                </a>
                <a href="{contact['github']}" target="_blank" class="social-link">
                    <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 .5A12 12 0 0 0 8.21 23.4c.6.11.82-.26.82-.58v-2.04c-3.34.73-4.04-1.6-4.04-1.6-.55-1.39-1.34-1.76-1.34-1.76-1.1-.75.08-.74.08-.74 1.22.09 1.87 1.26 1.87 1.26 1.08 1.84 2.83 1.31 3.52 1 .11-.77.42-1.3.76-1.6-2.66-.3-5.47-1.33-5.47-5.92 0-1.31.47-2.38 1.24-3.22-.12-.3-.54-1.52.12-3.16 0 0 1.02-.33 3.34 1.23a11.5 11.5 0 0 1 6.08 0c2.31-1.56 3.33-1.23 3.33-1.23.66 1.64.24 2.86.12 3.16.77.84 1.24 1.91 1.24 3.22 0 4.6-2.82 5.61-5.5 5.91.43.37.81 1.1.81 2.22v3.29c0 .32.21.7.83.58A12 12 0 0 0 12 .5z"/></svg>
                    <span class="social-value">GitHub</span>
                </a>
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_footer():
    st.markdown(
        """
        <div class="footer-note">Merci de votre visite.</div>
        """,
        unsafe_allow_html=True,
    )
