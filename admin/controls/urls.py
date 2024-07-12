from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'apicdats', views.ApiCdat, 'apicdats')
router.register(r'apicooviahorro', views.ApiCooviahorro, 'apicooviahorro')

urlpatterns = [
    path("cdats/", views.Cdat, name="cdats"),
    path("createcdat/", views.createCdat, name="createcdat"),
    path("cdats/updatecdat/<int:id>/", views.updatecdat, name="updatecdat"),
    path("deletecdat/<int:id>/", views.deletecdat, name="deletecdat"),
    
    path("cooviahorro/", views.Cooviahorro, name="cooviahorro"),
    path("createcooviahorro/", views.createCooviahorro, name="createcooviahorro"),
    path("deletecooviahorro/<int:id>/", views.deletecooviahorro, name="deletecooviahorro"),
    path("cooviahorro/updatecooviahorro/<int:id>/", views.updatecooviahorro, name="updatecooviahorro"),
    
    path("nosociales/", views.noSociales, name="nosociales"),
    path("createnosociales/", views.createNoSociales, name="createnosociales"),
    path("deletenosociales/<int:id>/", views.deleteNoSociales, name="deletenosociales"),
    path("nosociales/updatenosociales/<int:id>/", views.updateNoSociales, name="updatenosociales"),
    
    path("typesasociado/", views.typesAsociados, name="asociados"),
    path("createtypesasociado/", views.createTypesAsociados, name="createasociado"),
    path("deletetypeasociado/<int:id>/", views.deleteTypeAsociado, name="deleteasociado"),
    
    path("tasasnosociales/", views.tasasNoSociales, name="tasasnosociales"),
    path("tasascreatenosociales/", views.createTasasNoSociales, name="tasascreatenosociales"),
    path("tasasdeletenosociales/<int:id>/", views.deleteTasasNoSociales, name="tasasdeletenosociales"),
    path("tasasnosociales/updatetasasnosociales/<int:id>/", views.updateTasasNoSociales, name="tasasupdatenosociales"),
    
    path("administrables/", views.Admin, name="admin"),
    path("api/", include(router.urls))
]