def get_custom_css():
    return """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    :root {
        --bg: #07111f;
        --bg-soft: #0f172a;
        --panel: rgba(15, 23, 42, 0.9);
        --panel-strong: #111827;
        --line: rgba(148, 163, 184, 0.2);
        --text: #e2e8f0;
        --muted: #94a3b8;
        --primary: #60a5fa;
        --primary-strong: #3b82f6;
        --accent: #7c3aed;
        --success: #34d399;
    }

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        background: var(--bg);
        color: var(--text);
    }

    h1, h2, h3, .hero-title, .section-title {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background:
            radial-gradient(circle at top left, rgba(124, 58, 237, 0.20), transparent 32%),
            radial-gradient(circle at bottom right, rgba(59, 130, 246, 0.18), transparent 30%),
            var(--bg);
        color: var(--text);
    }

    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    [data-testid="stSidebarNav"] {
        display: none;
    }

    [data-testid="stSidebar"] {
        display: none;
    }

    .hero-shell {
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.96), rgba(17, 24, 39, 0.88));
        border: 1px solid var(--line);
        border-radius: 28px;
        padding: 2rem;
        box-shadow: 0 20px 45px rgba(2, 6, 23, 0.35);
    }

    .hero-title {
        font-size: 3.6rem;
        font-weight: 800;
        letter-spacing: -0.06em;
        background: linear-gradient(90deg, #7dd3fc 0%, #a78bfa 100%);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
        margin: 0 0 0.65rem 0;
        line-height: 1.02;
    }

    .hero-kicker {
        color: var(--accent);
        font-family: 'Inter', sans-serif;
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.16em;
        margin-bottom: 1rem;
    }

    .hero-subtitle {
        font-size: 1.15rem;
        color: var(--muted);
        font-weight: 500;
        margin-bottom: 1rem;
        letter-spacing: 0.01em;
    }

    .hero-location {
        display: inline-block;
        font-size: 0.82rem;
        text-transform: uppercase;
        letter-spacing: 0.12em;
        color: rgba(125, 211, 252, 0.9);
        background: rgba(96, 165, 250, 0.08);
        border: 1px solid rgba(96, 165, 250, 0.18);
        border-radius: 999px;
        padding: 0.45rem 0.7rem;
        margin-bottom: 1.2rem;
    }

    .hero-summary {
        color: var(--text);
        line-height: 1.7;
        font-size: 1.04rem;
        max-width: 650px;
        margin-bottom: 1.8rem;
    }

    .profile-frame {
        background: transparent;
        border: none;
        border-radius: 0;
        padding: 0;
        box-shadow: none;
        height: auto;
        min-height: 0;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-top: 0;
    }

    .profile-frame img,
    [data-testid="stImage"] img {
        width: 100%;
        max-width: 330px;
        height: 340px;
        object-fit: cover;
        border-radius: 4px;
        border: 1px solid var(--line);
        box-shadow: 0 18px 30px rgba(15, 23, 42, 0.45);
        display: block;
    }

    [data-testid="stImage"] {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 0;
    }

    .hero-actions {
        display: flex;
        flex-wrap: wrap;
        gap: 0.65rem;
        margin: 1.5rem 0 1.4rem 0;
    }

    .hero-link {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        min-height: 46px;
        padding: 0.75rem 1.1rem;
        border-radius: 3px;
        text-decoration: none;
        font-weight: 700;
        transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
        width: 100%;
        max-width: 220px;
    }

    .hero-link.primary {
        background: linear-gradient(135deg, rgba(96, 165, 250, 0.22), rgba(124, 58, 237, 0.26));
        border: 1px solid rgba(96, 165, 250, 0.35);
        color: var(--text);
        box-shadow: 0 12px 28px rgba(2, 6, 23, 0.18);
    }

    .hero-link.secondary {
        background: rgba(148, 163, 184, 0.04);
        border: 1px solid var(--line);
        color: var(--text);
    }

    .hero-link:hover {
        transform: translateY(-2px);
        box-shadow: 0 18px 30px rgba(96, 165, 250, 0.22);
        text-decoration: none;
    }

    .archive-return {
        margin-top: 1.2rem;
    }

    .archive-title {
        margin-top: 0.4rem !important;
    }

    .btn-row {
        display: flex;
        gap: 0.75rem;
        flex-wrap: wrap;
        margin-top: 0.7rem;
    }

    .btn-primary, .btn-secondary {
        text-decoration: none;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        min-height: 44px;
        padding: 0.72rem 1.2rem;
        border-radius: 12px;
        font-weight: 600;
        transition: all 0.3s ease;
    }

    .btn-primary {
        background: linear-gradient(135deg, var(--primary) 0%, var(--accent) 100%);
        color: white !important;
        box-shadow: 0 14px 24px rgba(96, 165, 250, 0.28);
    }

    .btn-primary:hover {
        transform: translateY(-2px);
        box-shadow: 0 18px 30px rgba(96, 165, 250, 0.34);
    }

    .btn-secondary {
        background: rgba(148, 163, 184, 0.05);
        color: var(--text);
        border: 1px solid var(--line);
    }

    .btn-secondary:hover {
        border-color: rgba(125, 211, 252, 0.5);
        color: var(--text);
        transform: translateY(-2px);
    }

    .project-archive {
        margin-top: 2rem;
        background: rgba(15, 23, 42, 0.5);
        border: 1px solid var(--line);
        border-radius: 4px;
        padding: 1.5rem;
    }

    .year-panel {
        margin: 1rem 0 1.5rem 0;
        padding: 0.8rem 1rem;
        border: 1px solid var(--line);
        border-radius: 12px;
        background: rgba(15, 23, 42, 0.7);
    }

    .year-group {
        margin-bottom: 1.2rem;
    }

    .year-label {
        font-size: 1.2rem;
        font-weight: 700;
        color: #dbeafe;
        margin: 0;
        padding-bottom: 0;
        border-bottom: none;
    }

    .month-group {
        margin-bottom: 1rem;
    }

    .month-label {
        font-size: 0.82rem;
        text-transform: uppercase;
        letter-spacing: 0.12em;
        color: var(--muted);
        margin: 0 0 0.6rem 0;
    }

    .archive-list {
        display: grid;
        gap: 0.7rem;
    }

    .archive-item {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 1rem;
        padding: 0.8rem 1rem;
        border: 1px solid var(--line);
        border-radius: 4px;
        background: var(--panel);
    }

    .archive-item a {
        color: var(--text);
        text-decoration: none;
        font-weight: 600;
        overflow-wrap: anywhere;
    }

    .archive-item a:hover {
        color: #7dd3fc;
    }

    .archive-date {
        font-size: 0.8rem;
        color: var(--muted);
        white-space: nowrap;
    }

    [data-testid="stDownloadButton"] button {
        background: rgba(147, 197, 253, 0.08) !important;
        border: 1px solid rgba(125, 211, 252, 0.4) !important;
        color: var(--text) !important;
        border-radius: 12px !important;
        font-weight: 600 !important;
        min-height: 44px !important;
        transition: all 0.3s ease !important;
    }

    [data-testid="stDownloadButton"] button:hover {
        transform: translateY(-2px) !important;
        border-color: rgba(125, 211, 252, 0.8) !important;
        background: rgba(96, 165, 250, 0.1) !important;
    }

    .section-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: var(--text);
        margin-top: 3rem;
        margin-bottom: 1.4rem;
        padding-bottom: 0.8rem;
        border-bottom: 1px solid var(--line);
    }

    .skill-grid,
    .project-grid,
    .contact-grid {
        display: grid;
        gap: 1.2rem;
    }

    .skill-grid {
        grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    }

    .skill-card,
    .project-card,
    .contact-panel {
        background: linear-gradient(180deg, rgba(17, 24, 39, 0.96), rgba(15, 23, 42, 0.9));
        border: 1px solid var(--line);
        border-radius: 20px;
        padding: 1.3rem 1.2rem;
        box-shadow: 0 16px 28px rgba(2, 6, 23, 0.18);
    }

    .skill-card h3,
    .project-card h3,
    .contact-panel h3 {
        margin: 0 0 0.85rem 0;
        color: var(--text);
        font-size: 1.12rem;
        font-weight: 700;
    }

    .tech-badge {
        display: inline-block;
        margin: 0 0.45rem 0.5rem 0;
        padding: 0.42rem 0.7rem;
        border-radius: 999px;
        background: rgba(96, 165, 250, 0.08);
        border: 1px solid rgba(96, 165, 250, 0.22);
        color: #bfdbfe;
        font-size: 0.76rem;
        font-weight: 600;
    }

    .project-grid {
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    }

    .project-row-gap {
        height: 1rem;
    }

    .project-card {
        display: flex;
        flex-direction: column;
        height: auto;
        min-height: 0;
        box-sizing: border-box;
        transition: transform 0.25s ease, border-color 0.25s ease;
    }

    .project-index {
        color: var(--primary);
        font-family: 'Inter', sans-serif;
        font-size: 0.8rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        margin-bottom: 1.2rem;
    }

    .project-card:hover {
        transform: translateY(-4px);
        border-color: rgba(125, 211, 252, 0.5);
    }

    .project-card h3 {
        font-size: 1.32rem;
        margin-bottom: 0.8rem;
    }

    .project-card p {
        color: var(--muted);
        line-height: 1.7;
        margin: 0.5rem 0 1rem 0;
        flex-grow: 1;
        overflow-wrap: anywhere;
    }

    .project-link {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        color: #dbeafe;
        text-decoration: none;
        font-weight: 600;
        transition: color 0.2s ease;
        margin-top: auto;
    }

    .project-link:hover {
        color: #7dd3fc;
    }

    .contact-grid {
        grid-template-columns: 1.2fr 1fr;
    }

    .contact-panel {
        min-height: 100%;
    }

    .contact-form label,
    .contact-panel label {
        color: var(--text);
        font-weight: 600;
    }

    .social-link {
        display: flex;
        align-items: center;
        gap: 0.8rem;
        color: var(--muted);
        text-decoration: none;
        padding: 0.75rem 0.9rem;
        border-radius: 14px;
        border: 1px solid rgba(148, 163, 184, 0.12);
        background: rgba(15, 23, 42, 0.45);
        transition: all 0.25s ease;
        margin-bottom: 0.7rem;
    }

    .social-link:last-child {
        margin-bottom: 0;
    }

    .social-link:hover {
        background: rgba(96, 165, 250, 0.08);
        border-color: rgba(125, 211, 252, 0.25);
        color: var(--text);
        transform: translateX(2px);
    }

    .social-link svg {
        width: 18px;
        height: 18px;
        fill: currentColor;
        flex-shrink: 0;
        opacity: 0.9;
    }

    .social-value {
        color: var(--text);
        font-weight: 600;
        letter-spacing: 0.01em;
        word-break: break-word;
    }

    .footer-note {
        text-align: center;
        color: var(--muted);
        border-top: 1px solid var(--line);
        padding-top: 1.4rem;
        margin-top: 2rem;
        font-size: 0.92rem;
    }

    @media (max-width: 760px) {
        .main .block-container {
            padding: 1.5rem 1rem 3rem 1rem;
        }

        .hero-title {
            font-size: 2.55rem;
        }

        .profile-frame img,
        [data-testid="stImage"] img {
            height: 260px;
            max-width: 260px;
        }

        .contact-grid {
            grid-template-columns: 1fr;
        }

        .hero-shell {
            padding: 1.3rem;
        }

        .hero-link {
            max-width: none;
        }
    }
    </style>
    """
