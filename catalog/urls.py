from django.urls import path
from . import views
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    path("index.html", views.index),
    path("agent.html", views.agent),
    path("properties.html", views.properties),
    path("properties-single.html", views.properties_single),
    path("about.html", views.about),
    path("contact.html", views.contact),
]
