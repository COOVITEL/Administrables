from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'apicdats', views.ApiCdat, 'apicdats')
router.register(r'apicooviahorro', views.ApiCooviahorro, 'apicooviahorro')

urlpatterns = [
    path("creditos/", views.creditos, name="creditos"),
    path("administrables/", views.Admin, name="admin"),
    path("api/", include(router.urls)),
    path('api/simuladorcredito/', views.SimuladorCreditoApiView.as_view(), name='apisimuladorcredito'),
    path('api/rotativos/', views.RotativoApi.as_view(), name="apirotativos")
]