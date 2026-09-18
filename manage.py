#!/usr/bin/env python
"""Run Django commands from the project root."""
import os
import sys
from pathlib import Path


def main():
    project_root = Path(__file__).resolve().parent
    backend_dir = project_root / "backend"
    sys.path.insert(0, str(backend_dir))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.config.settings")

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
