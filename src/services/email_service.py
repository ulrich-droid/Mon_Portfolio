import os
import smtplib
from email.message import EmailMessage
from pathlib import Path

import streamlit as st


def _load_dotenv_values():
    project_root = Path(__file__).resolve().parents[2]
    candidate_files = [project_root / ".env", project_root / ".env.example"]

    for env_path in candidate_files:
        if not env_path.exists():
            continue

        for line in env_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


_load_dotenv_values()


def _get_setting(name: str, default: str | None = None) -> str | None:
    try:
        secret_value = st.secrets.get(name)
    except Exception:
        secret_value = None

    return str(secret_value) if secret_value is not None else os.getenv(name, default)


def send_contact_email(name: str, email: str, message: str) -> tuple[bool, str]:
    """Send a contact message to the configured recipient email.

    Uses Gmail SMTP by default, and reads settings from environment variables or a .env file.
    """
    host = _get_setting("SMTP_HOST", "smtp.gmail.com")
    port = _get_setting("SMTP_PORT", "587")
    username = _get_setting("SMTP_USERNAME") or _get_setting("SMTP_TO") or "ulricharegba@gmail.com"
    password = _get_setting("SMTP_PASSWORD")
    recipient = os.getenv("SMTP_TO") or os.getenv("CONTACT_EMAIL") or "ulricharegba@gmail.com"

    if not password:
        return False, (
            "Le mot de passe SMTP n'est pas configuré. Ajoute SMTP_PASSWORD dans les variables d'environnement "
            "ou dans le fichier .env (exemple : SMTP_PASSWORD=xxxxxxxx)."
        )

    try:
        msg = EmailMessage()
        msg["Subject"] = f"Nouveau message du portfolio : {name}"
        msg["From"] = username
        msg["To"] = recipient
        msg.set_content(
            f"Nom: {name}\n"
            f"Email: {email}\n\n"
            f"Message:\n{message}"
        )

        with smtplib.SMTP(host, int(port)) as server:
            use_tls = os.getenv("SMTP_USE_TLS", "true").lower() == "true"
            if use_tls:
                server.starttls()
            server.login(username, password)
            server.send_message(msg)

        return True, "Message envoyé avec succès."
    except Exception as exc:
        return False, f"Échec de l'envoi : {exc}"
