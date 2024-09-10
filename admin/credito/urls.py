from django.urls import path
from . import views


urlpatterns = [
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
    
    path("fidelizacion/", views.fidelizacion, name="fidelizacion"),
    path("createfidelizacion/", views.createfidelizacion, name="createfidelizacion"),
    path("deletefidelizacion/<int:id>/", views.deletefidelizacion, name="deletefidelizacion"),
    path("fidelizacion/updatefidelizacion/<int:id>/", views.updatefidelizacion, name="updatefidelizacion"),
    
    path("sociales/", views.sociales, name="sociales"),
    path("createsociales/", views.createsociales, name="createsociales"),
    path("deletesociales/<int:id>/", views.deletesociales, name="deletesociales"),
    path("sociales/updatesociales/<int:id>/", views.updatesociales, name="updatesociales"),
    
    path("asociadotype/", views.asociadosType, name="asociadostype"),
    path("createasociadotype/", views.createasociadosType, name="createasociadotype"),
    path("deleteaosicadotype/<int:id>/", views.deleteasociadosType, name="deleteasociadotype"),
]