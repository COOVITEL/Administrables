from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'apicdats', views.ApiCdat, 'apicdats')
router.register(r'apicooviahorro', views.ApiCooviahorro, 'apicooviahorro')

urlpatterns = [
    path("cdats/", views.Cdat, name="cdats"),
    path("createcdat/", views.createCdat, name="createcdat"),
    path("creditos/", views.creditos, name="creditos"),
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

    path("ajustes/ajustescore", views.ajustesScore, name="ajustescore"),
    path("ajustes/create/ajustescore", views.createAjustesScore, name="createajustescore"),
    path("ajustes/update/ajustescore/<int:id>", views.updateAjustesScore, name="updateajustescore"),
    path("ajustes/delete/ajustescore/<int:id>", views.deleteAjustesScore, name="deleteajustescore"),
    
    path("ajustes/ajustesaporte", views.ajustesAporte, name="ajusteaporte"),
    path("ajustes/create/ajusteaportes", views.createAjustesAporte, name="createajusteaporte"),
    path("ajustes/update/ajusteaporte/<int:id>", views.updateAjustesAporte, name="updateajusteaporte"),
    path("ajustes/delete/ajusteaporte/<int:id>", views.deleteAjustesAporte, name="deleteajusteaporte"),
    
    path("ajustes/ajustesplazo", views.ajustesPlazo, name="ajusteplazo"),
    path("ajustes/create/ajusteplazo", views.createAjustesPlazo, name="createajusteplazo"),
    path("ajustes/update/ajusteplazo/<int:id>", views.updateAjustesPlazo, name="updateajusteplazo"),
    path("ajustes/delete/ajusteplazo/<int:id>", views.deleteAjustesPlazo, name="deleteajusteplazo"),
    
    path("ajustes/ajustescdat", views.ajustesCDAT, name="ajustecdat"),
    path("ajustes/create/ajustecdat", views.createAjustesCDAT, name="createajustecdat"),
    path("ajustes/update/ajustecdat/<int:id>", views.updateAjustesCDAT, name="updateajustecdat"),
    path("ajustes/delete/ajustecdat/<int:id>", views.deleteAjustesCDAT, name="deleteajustecdat"),
    
    path("ajustes/ajustescooviahorro", views.ajustesCooviahorro, name="ajustecooviahorro"),
    path("ajustes/create/ajustecooviahorro", views.createAjustesCooviahorro, name="createajustecooviahorro"),
    path("ajustes/update/ajustecooviahorro/<int:id>", views.updateAjustesCooviahorro, name="updateajustecooviahorro"),
    path("ajustes/delete/ajustecooviahorro/<int:id>", views.deleteAjustesCooviahorro, name="deleteajustecooviahorro"),

    path("ajustes/descuentos", views.descuentos, name="descuentos"),
    path("ajustes/create/descuento", views.createDescuentos, name="createdescuento"),
    path("ajustes/update/descuento/<int:id>", views.updateDescuentos, name="updatedescuento"),
    path("ajustes/delete/ajustedescuento/<int:id>", views.deleteDescuentos, name="deletedescuento"),

    path("administrables/", views.Admin, name="admin"),
    path("api/", include(router.urls)),
    path('api/simuladorcredito/', views.SimuladorCreditoApiView.as_view(), name='apisimuladorcredito'),
]