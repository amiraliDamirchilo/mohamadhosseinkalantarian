# Mohamad Kalantarian website

This website is a Django application with a plain HTML, CSS, and JavaScript frontend.

Run it from this folder:

```powershell
pip install -r requirements.txt
py manage.py migrate
py manage.py runserver
```

See [backend/README.md](backend/README.md) for admin-panel instructions.

## Vercel

This repository is ready for a Django deployment on Vercel. Import the repository with its root directory set to this folder; do not set a Node.js build command or an output directory. Vercel detects `manage.py` and `requirements.txt` automatically.
