from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r"registros-creditos", RegistroCreditosView, "registros-creditos")
router.register(r"registros-rotativos", RegistroRotativoView, "registros-rotativos")
router.register(r"registros-cooviahorro", RegistroCooviahorroView, "registros-cooviahorro")

urlpatterns = [
    path("", include(router.urls))
]