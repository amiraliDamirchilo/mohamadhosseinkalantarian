from django.db import models


class SiteContent(models.Model):
    """A named piece of copy shown anywhere on the website."""

    key = models.SlugField(unique=True, help_text="Stable API key, e.g. hero_title")
    value = models.TextField()
    description = models.CharField(max_length=180, blank=True)

    class Meta:
        verbose_name = "Site text"
        verbose_name_plural = "Site texts"
        ordering = ["key"]

    def __str__(self):
        return self.key


class Service(models.Model):
    title = models.CharField(max_length=160)
    description = models.TextField()
    sort_order = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ["sort_order", "id"]

    def __str__(self):
        return self.title


class PortfolioCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Portfolio category"
        verbose_name_plural = "Portfolio categories"
        ordering = ["sort_order", "name"]

    def __str__(self):
        return self.name


class PortfolioProject(models.Model):
    title = models.CharField(max_length=180)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(PortfolioCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name="projects")
    image = models.URLField(blank=True, help_text="Public image URL, or a path such as /ravia-villa.jpg")
    image_alt = models.CharField(max_length=180, blank=True)
    description = models.TextField()
    architect = models.CharField(max_length=180, blank=True)
    scope = models.CharField(max_length=250, blank=True)
    sort_order = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Portfolio project"
        verbose_name_plural = "Portfolio projects"
        ordering = ["sort_order", "id"]

    def __str__(self):
        return self.title


class PortfolioMedia(models.Model):
    IMAGE = "image"
    VIDEO = "video"
    MEDIA_TYPES = [(IMAGE, "Image"), (VIDEO, "Video")]

    project = models.ForeignKey(PortfolioProject, on_delete=models.CASCADE, related_name="media")
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES)
    file_url = models.URLField(help_text="ImageKit URL")
    imagekit_file_id = models.CharField(max_length=160, blank=True, editable=False)
    alt_text = models.CharField(max_length=180, blank=True)
    caption = models.CharField(max_length=240, blank=True)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Work media"
        verbose_name_plural = "Work media"
        ordering = ["sort_order", "id"]

    def __str__(self):
        return f"{self.project}: {self.get_media_type_display()}"
