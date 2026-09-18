import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
app = get_wsgi_application()
# Django tooling commonly looks for ``application``; Vercel looks for ``app``.
application = app
