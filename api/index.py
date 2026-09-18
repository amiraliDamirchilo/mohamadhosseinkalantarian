"""Explicit Vercel Function entry point for the Django WSGI app."""
import os
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "backend"))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.config.settings")

from backend.config.wsgi import app  # noqa: E402
