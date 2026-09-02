from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
ASSETS_DIR = BASE_DIR / "assets"

PHOTO_PATH = str(ASSETS_DIR / "AREGBA photo identité .jpeg")
CV_PATH = str(ASSETS_DIR / "CV_ULRICH_AREGBA-TISSOU.pdf")

PROFILE = {
    "name": "Ulrich Tchokoute AREGBA-TISSOU",
    "title": "Étudiant en Master IA & Big Data",
    "location": "Lomé, Togo",
    "summary": (
        "Spécialisé dans la conception d'architectures de données robustes et "
        "le développement de modèles d'intelligence artificielle. "
        "Mon approche allie l'ingénierie Big Data et l'application de solutions "
        "Deep Learning avancées."
    ),
    "photo_url": "",
}

SKILLS = {
    "Intelligence Artificielle & NLP": [
        "PyTorch",
        "Hugging Face",
        "SpaCy",
        "Tensorflow",
        "sklearn",
        "NLTK",
    ],
    "Data Engineering & Architectures": [
        "Apache Kafka",
        "Apache Spark",
        "PostgreSQL",
        "MongoDB",
        "Talend",
        "Docker",
        "Databricks",
    ],
}

PROJECTS = [
    {
        "title": "ExploreTogo : Pipeline Big Data & Streaming",
        "stack": ["Docker", "Kafka", "Spark", "Metabase", "Talend", "PostgreSQL", "MongoDB"],
        "description": (
            "Conception d'une infrastructure de données conteneurisée complexe intégrant "
            "des flux de données en temps réel. Mise en place de bases de données "
            "relationnelles et NoSQL, orchestrées pour alimenter des tableaux de bord "
            "analytiques interactifs."
        ),
        "link": "https://github.com/ulrich-droid/ExploreTogo",
        "label": "Consulter le code source sur github",
        "year": 2026,
        "month": "Avril",
    },
    {
        "title": "Traduction Automatique Neurale (English - French - Éwé)",
        "stack": ["NLP", "NLLB-200", "LoRA", "re", "huggingface"],
        "description": (
            "Constitution d'un corpus de textes parallèles et fine-tuning de modèles de "
            "langages spécialisés. Évaluation des performances de traduction sur des "
            "langues peu dotées à l'aide de métriques standardisées."
        ),
        "link": "https://github.com/ulrich-droid/translation-ee-ang-fr",
        "label": "Consulter le code source sur github",
        "year": 2026,
        "month": "Mai",
    },
    {
        "title": "Analyseur de Sentiments & Extracteur de Données",
        "stack": ["Tensorflow", "SpaCy", "Apache Tika"],
        "description": (
            "Développement d'un pipeline d'analyse exploitant Tensorflow pour la "
            "classification de sentiments. Création d'un outil de parsing automatisé "
            "pour l'extraction structurée d'informations (noms, contacts) issues de "
            "documents non formatés."
        ),
        "link": "https://github.com/ulrich-droid/sentiment-parser",
        "label": "Consulter le code source sur github",
        "year": 2026,
        "month": "Juillet",
    },
    {
        "title": "Détection d'anomalies dans les transactions bancaires avec K-means",
        "stack": ["scikit-learn", "matplotlib", "pandas","numpy"],
        "description": (
            "Détection des transactions financières anormales (fraudes potentielles)"
            " à partir d'un clustering K-means non supervisé, après une analyse exploratoire"
            " des données (EDA) qui justifie les choix du pipeline."
        ),
        "link": "https://github.com/ulrich-droid/Anomaly-detection-in-banking-transactions-with-kmeans",
        "label": "Consulter le code source sur github",
        "year": 2026,
        "month": "Mai",
    },
    {
        "title": "Data Analyst IoT : Évaluation de la qualité des données, détection d'anomalies sur capteurs agricole",
        "stack": ["seaborn", "matplotlib", "pandas", "numpy", "Folium"],
        "description": (
            "Détection des anomalies et proposition d'actions de maintenance appropriées en analysant les données météorologiques du sol d'un village."
        ),
        "link": "https://github.com/ulrich-droid/Data-Analyst-IoT",
        "label": "Consulter le code source sur github",
        "year": 2026,
        "month": "Mai",
    },
    {
        "title": "Tableau de bord : Crimes de masse aux États-Unis",
        "stack": ["PowerBI"],
        "description": (
            "Analyse des corrélations entre les crimes de masse aux États-Unis"
            "et divers indicateurs socio-économiques et politiques (coût de la vie, richesse locale,"
            "accès aux armes, stupéfiants, criminalité, chômage, PIB et partis politiques dominants"
            ),
        "link": "https://github.com/ulrich-droid/crimes-de-masse-aux-usa",
        "label": "Consulter le code source sur github",
        "year": 2026,
        "month": "Janvier",
    },
]

RECENT_PROJECTS = [
    "ExploreTogo : Pipeline Big Data & Streaming",
    "Traduction Automatique Neurale (English - French - Éwé)",
    "Analyseur de Sentiments & Extracteur de Données",
    "Détection d'anomalies dans les transactions bancaires avec K-means",
    "Data Analyst IoT : Évaluation de la qualité des données, détection d'anomalies sur capteurs agricole",
    "Tableau de bord : Crimes de masse aux États-Unis",
]

CONTACT = {
    "email": "ulricharegba@gmail.com",
    "phone": "+228 91 10 81 61",
    "linkedin": "https://www.linkedin.com/in/ulrich-aregba",
    "github": "https://github.com/ulrich-droid",
}


def get_photo_url():
    if Path(PHOTO_PATH).exists():
        return PHOTO_PATH

    return (
        "https://images.unsplash.com/photo-1568602471122-7832951cc4c5"
        "?auto=format&fit=crop&w=300&q=80"
    )


def get_profile():
    profile = dict(PROFILE)
    profile["photo_url"] = get_photo_url()
    return profile


def get_skills():
    return {category: list(items) for category, items in SKILLS.items()}


def get_projects():
    return [dict(project) for project in PROJECTS]


def get_recent_projects():
    projects_by_title = {project["title"]: project for project in PROJECTS}
    return [dict(projects_by_title[title]) for title in RECENT_PROJECTS if title in projects_by_title]


def get_contact():
    return dict(CONTACT)


def get_cv_filename():
    if Path(CV_PATH).exists():
        return "CV_ULRICH_AREGBA-TISSOU.pdf"

    cv_path = ASSETS_DIR / "cv.pdf"
    if cv_path.exists():
        return "cv.pdf"

    pdf_files = sorted(ASSETS_DIR.glob("*.pdf"))
    if pdf_files:
        return pdf_files[0].name

    return "CV.pdf"


def get_cv_bytes():
    if Path(CV_PATH).exists():
        return Path(CV_PATH).read_bytes()

    cv_path = ASSETS_DIR / "cv.pdf"
    if cv_path.exists():
        return cv_path.read_bytes()

    pdf_files = sorted(ASSETS_DIR.glob("*.pdf"))
    if pdf_files:
        return pdf_files[0].read_bytes()

    return b"CV non disponible. Ajoutez un fichier PDF dans le dossier assets/."
