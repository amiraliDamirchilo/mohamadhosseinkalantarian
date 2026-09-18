# Generated manually for this small project.
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(name="PortfolioCategory", fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("name", models.CharField(max_length=100, unique=True)),
            ("slug", models.SlugField(unique=True)),
            ("sort_order", models.PositiveIntegerField(default=0)),
        ], options={"verbose_name": "Portfolio category", "verbose_name_plural": "Portfolio categories", "ordering": ["sort_order", "name"]}),
        migrations.CreateModel(name="Service", fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("title", models.CharField(max_length=160)), ("description", models.TextField()),
            ("sort_order", models.PositiveIntegerField(default=0)), ("is_published", models.BooleanField(default=True)),
        ], options={"ordering": ["sort_order", "id"]}),
        migrations.CreateModel(name="SiteContent", fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("key", models.SlugField(help_text="Stable API key, e.g. hero_title", unique=True)),
            ("value", models.TextField()), ("description", models.CharField(blank=True, max_length=180)),
        ], options={"verbose_name": "Site text", "verbose_name_plural": "Site texts", "ordering": ["key"]}),
        migrations.CreateModel(name="PortfolioProject", fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("title", models.CharField(max_length=180)), ("slug", models.SlugField(unique=True)),
            ("image", models.URLField(blank=True, help_text="Public image URL, or a path such as /ravia-villa.jpg")),
            ("image_alt", models.CharField(blank=True, max_length=180)), ("description", models.TextField()),
            ("architect", models.CharField(blank=True, max_length=180)), ("scope", models.CharField(blank=True, max_length=250)),
            ("sort_order", models.PositiveIntegerField(default=0)), ("is_published", models.BooleanField(default=True)),
            ("category", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="projects", to="website.portfoliocategory")),
        ], options={"verbose_name": "Portfolio project", "verbose_name_plural": "Portfolio projects", "ordering": ["sort_order", "id"]}),
    ]
