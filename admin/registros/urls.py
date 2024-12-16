from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r"registros-creditos", RegistroCreditosView, "registros-creditos")

urlpatterns = [
    path("registros/", include(router.urls))
]