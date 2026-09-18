from django.core.management.base import BaseCommand

from website.models import PortfolioCategory, PortfolioProject, Service, SiteContent


class Command(BaseCommand):
    help = "Create the initial English website content. Safe to run more than once."

    def handle(self, *args, **options):
        texts = {
            "site_name": "Mohamad Kalantarian",
            "nav_services": "Services",
            "nav_work": "Work",
            "nav_contact": "Contact",
            "hero_label": "BIM Specialist · Revit Modeler",
            "hero_title": "Clear models.\nAccurate outcomes.",
            "hero_intro": "I help architects and AEC teams turn drawings, designs, and point clouds into accurate Revit BIM models.",
            "hero_cta": "Start a project ↗",
            "services_label": "01 / Services",
            "services_title": "What I do",
            "work_label": "02 / Selected work",
            "work_title": "Projects",
            "about_label": "03 / About",
            "about_title": "Mohamad Kalantarian",
            "about_text": "I work with architects and AEC teams to create reliable Revit models with a focus on clarity, coordination, and buildable detail.",
            "contact_label": "Have a project in mind?",
            "contact_title": "Let's work together.",
            "email": "mh.kalantaryan@gmail.com",
            "footer_role": "BIM Specialist · Revit Modeler",
            "architect_label": "Architect",
            "scope_label": "Scope",
            "telegram_label": "Telegram ↗",
            "instagram_label": "Instagram ↗",
            "linkedin_label": "LinkedIn ↗",
        }
        for key, value in texts.items():
            SiteContent.objects.update_or_create(key=key, defaults={"value": value})
        Service.objects.get_or_create(title="Architectural BIM Modeling", defaults={"description": "Accurate Revit models developed from architectural drawings, design intent, and construction requirements.", "sort_order": 1})
        Service.objects.get_or_create(title="Point Cloud to BIM", defaults={"description": "Precise as-built Revit models created from point-cloud scans for renovation and documentation projects.", "sort_order": 2})
        Service.objects.get_or_create(title="Custom Revit Families", defaults={"description": "Clean, parametric families made for project-specific architectural elements and components.", "sort_order": 3})
        category, _ = PortfolioCategory.objects.get_or_create(name="Residential", defaults={"slug": "residential", "sort_order": 1})
        PortfolioProject.objects.get_or_create(title="Ravia Villa", defaults={"slug": "ravia-villa", "category": category, "image": "/ravia-villa.jpg", "image_alt": "BIM details and exterior views of Ravia Villa", "description": "A two-story villa translated from architectural design into a detailed, practical Revit model. My work covered interior details, the façade, and its technical connections.", "architect": "Ahmad Saffar", "scope": "BIM modeling and detail development", "sort_order": 1})
        PortfolioProject.objects.get_or_create(title="Qeshm Vernacular Villa", defaults={"slug": "qeshm-vernacular-villa", "category": category, "image": "/qeshm-villa.jpg", "image_alt": "Qeshm Vernacular Villa", "description": "A contemporary vernacular villa inspired by Qeshm Island’s climate, local materials, and traditions. My role covered BIM modeling, architectural detailing, and construction documentation.", "architect": "Mohammad Hassan Forouzanfar", "scope": "BIM, documentation, and coordination", "sort_order": 2})
        self.stdout.write(self.style.SUCCESS("Initial website content is ready."))
