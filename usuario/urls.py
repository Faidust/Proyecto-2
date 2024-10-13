from django.urls import path
from . import views

urlpatterns=[
    path("usuario/", views.usuario),
    path("logout/", views.exit),
]