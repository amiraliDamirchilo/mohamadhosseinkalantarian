from django.http import JsonResponse
from django.shortcuts import render

from .models import PortfolioCategory, PortfolioProject, Service, SiteContent


def home(request):
    return render(request, "website/index.html")


def site_content(request):
    return JsonResponse({item.key: item.value for item in SiteContent.objects.all()})


def services(request):
    data = [{"id": item.id, "title": item.title, "description": item.description} for item in Service.objects.filter(is_published=True)]
    return JsonResponse(data, safe=False)


def categories(request):
    data = [{"id": item.id, "name": item.name, "slug": item.slug} for item in PortfolioCategory.objects.all()]
    return JsonResponse(data, safe=False)


def projects(request):
    category = request.GET.get("category")
    queryset = PortfolioProject.objects.filter(is_published=True).select_related("category").prefetch_related("media")
    if category:
        queryset = queryset.filter(category__slug=category)
    data = [{
        "id": item.id, "title": item.title, "slug": item.slug,
        "category": item.category.slug if item.category else None,
        "image": item.image, "image_alt": item.image_alt, "description": item.description,
        "architect": item.architect, "scope": item.scope,
        "media": [{
            "type": media.media_type, "url": media.file_url, "alt": media.alt_text,
            "caption": media.caption,
        } for media in item.media.all()],
    } for item in queryset]
    return JsonResponse(data, safe=False)
