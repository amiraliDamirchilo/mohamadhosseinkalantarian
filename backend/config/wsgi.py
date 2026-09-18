import os
import sys
from pathlib import Path

from django.core.wsgi import get_wsgi_application

# Vercel imports this file directly from the repository root. Make the Django
# app directory importable before loading settings and installed applications.
BACKEND_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BACKEND_DIR))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.config.settings")
app = get_wsgi_application()
# Django tooling commonly looks for ``application``; Vercel looks for ``app``.
application = app
