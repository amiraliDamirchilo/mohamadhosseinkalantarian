import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("website", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="PortfolioMedia",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("media_type", models.CharField(choices=[("image", "Image"), ("video", "Video")], max_length=10)),
                ("file_url", models.URLField(help_text="ImageKit URL")),
                ("imagekit_file_id", models.CharField(blank=True, editable=False, max_length=160)),
                ("alt_text", models.CharField(blank=True, max_length=180)),
                ("caption", models.CharField(blank=True, max_length=240)),
                ("sort_order", models.PositiveIntegerField(default=0)),
                ("project", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="media", to="website.portfolioproject")),
            ],
            options={"verbose_name": "Work media", "verbose_name_plural": "Work media", "ordering": ["sort_order", "id"]},
        ),
    ]
