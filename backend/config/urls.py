from django.contrib import admin
from django.urls import include, path

from website import views

urlpatterns = [
    path("", views.home, name="home"),
    path("admin/", admin.site.urls),
    path("api/", include("website.urls")),
]
