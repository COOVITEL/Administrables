from django.urls import path
from . import views

urlpatterns = [
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
]
