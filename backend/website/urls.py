from django.urls import path

from . import views

urlpatterns = [
    path("content/", views.site_content, name="site-content"),
    path("services/", views.services, name="services"),
    path("portfolio/categories/", views.categories, name="portfolio-categories"),
    path("portfolio/projects/", views.projects, name="portfolio-projects"),
]
