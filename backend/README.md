# Django website

The public site is rendered by Django with plain HTML, CSS, and JavaScript. No Next.js or Node.js runtime is required.

## Start locally

```powershell
cd ..
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
py manage.py migrate
py manage.py seed_website
py manage.py createsuperuser
py manage.py runserver
```

Open `http://127.0.0.1:8000/admin/` to change English site copy, services, portfolio categories, and portfolio projects.

## Images and videos

Open a **Portfolio project** in the admin panel. Use **Cover upload** for its primary image, then use the **Work media** table to add any number of images or videos. Files are uploaded directly from Django to ImageKit and their delivery URLs are saved automatically.

ImageKit credentials belong in `backend/.env`; copy `backend/.env.example` if you need to configure a new environment. Do not commit the private key.

Public API endpoints:

- `/api/content/`
- `/api/services/`
- `/api/portfolio/categories/`
- `/api/portfolio/projects/` (use `?category=residential` to filter)

`DATABASE_URL` is temporarily embedded in `config/settings.py` as requested. Set `DATABASE_URL` as an environment variable before deployment so it overrides the temporary value.
