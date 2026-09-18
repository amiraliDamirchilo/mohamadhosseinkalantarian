from django import forms
from django.contrib import admin
from django.core.exceptions import ValidationError

from .imagekit import upload_media
from .models import PortfolioCategory, PortfolioMedia, PortfolioProject, Service, SiteContent

admin.site.site_header = "Mohamad Kalantarian Website Admin"
admin.site.site_title = "Website Admin"
admin.site.index_title = "Content management"


@admin.register(SiteContent)
class SiteContentAdmin(admin.ModelAdmin):
    list_display = ("key", "description")
    search_fields = ("key", "value", "description")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "sort_order", "is_published")
    list_editable = ("sort_order", "is_published")
    search_fields = ("title", "description")


@admin.register(PortfolioCategory)
class PortfolioCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "sort_order")
    list_editable = ("sort_order",)
    prepopulated_fields = {"slug": ("name",)}


class PortfolioProjectForm(forms.ModelForm):
    image = forms.URLField(required=False, widget=forms.HiddenInput())
    cover_upload = forms.FileField(required=False, label="Cover image", help_text="Choose an image file from your computer. It is uploaded to ImageKit when you save.")
    field_order = ("title", "slug", "category", "cover_upload", "image_alt", "description", "architect", "scope", "sort_order", "is_published")

    class Meta:
        model = PortfolioProject
        fields = "__all__"

    def clean_cover_upload(self):
        file = self.cleaned_data.get("cover_upload")
        if file:
            if not file.content_type.startswith("image/"):
                raise ValidationError("The project cover must be an image.")
            self._cover_upload = upload_media(file, folder="/portfolio/covers")
        return file

    def save(self, commit=True):
        instance = super().save(commit=False)
        file = self.cleaned_data.get("cover_upload")
        if file:
            instance.image = self._cover_upload["url"]
        if commit:
            instance.save()
            self.save_m2m()
        return instance


class PortfolioMediaForm(forms.ModelForm):
    upload = forms.FileField(required=False, help_text="Upload an image or video to ImageKit. It replaces the ImageKit URL field.")

    class Meta:
        model = PortfolioMedia
        fields = ("media_type", "alt_text", "caption", "sort_order")

    def clean_upload(self):
        file = self.cleaned_data.get("upload")
        if file and not (file.content_type.startswith("image/") or file.content_type.startswith("video/")):
            raise ValidationError("Only image and video files are supported.")
        return file

    def clean(self):
        cleaned = super().clean()
        file = cleaned.get("upload")
        media_type = cleaned.get("media_type")
        if media_type and not file and not self.instance.pk:
            self.add_error("upload", "Upload a file or provide an ImageKit URL.")
        if file and media_type and not file.content_type.startswith(f"{media_type}/"):
            self.add_error("upload", f"Select a {media_type} file for the selected media type.")
        if file and not self.errors:
            self._media_upload = upload_media(file, folder="/portfolio/work-media")
        return cleaned

    def save(self, commit=True):
        instance = super().save(commit=False)
        file = self.cleaned_data.get("upload")
        if file:
            instance.file_url = self._media_upload["url"]
            instance.imagekit_file_id = self._media_upload["file_id"]
        if commit:
            instance.save()
            self.save_m2m()
        return instance


class PortfolioMediaInline(admin.TabularInline):
    model = PortfolioMedia
    form = PortfolioMediaForm
    extra = 1
    fields = ("media_type", "upload", "alt_text", "caption", "sort_order")


@admin.register(PortfolioProject)
class PortfolioProjectAdmin(admin.ModelAdmin):
    form = PortfolioProjectForm
    inlines = (PortfolioMediaInline,)
    list_display = ("title", "category", "sort_order", "is_published")
    list_filter = ("category", "is_published")
    list_editable = ("sort_order", "is_published")
    search_fields = ("title", "description", "architect", "scope")
    prepopulated_fields = {"slug": ("title",)}
