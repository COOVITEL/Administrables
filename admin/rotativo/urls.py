from django.urls import path
from . import views

urlpatterns = [
    path("controls_rotativos/", views.controlRotativos, name="controlsRotativos"),
    
    path("asociadoRotativo/", views.typesAsociadosRotativos, name="asociadosrotativo"),
    path("created/asociadoRotatico/", views.createTypeAsociado, name="createAsociadoRotativo"),
    path("deleteAsociadoRotativo/<int:id>/", views.deleteTypeAsociado, name="deleteAsociadoRotativo"),
    path("update/asociadoRotativo/<int:id>/", views.updateTypeAsociado, name="updateAsociadoRotativo"),
    
    path("rotativos/", views.rotativos, name="rotativos"),
    path("createrotativo/", views.createRotativo, name="createrotativo"),
    path("deleterotativo/<int:id>/", views.deleteRotativo, name="deleterotativo"),
    path("updaterotativo/<int:id>/", views.updateRotativo, name="updaterotativo"),
    
    path("rotativos/escenarios", views.escenarios, name="escenarios"),
    path("rotativos/createescenario/", views.createEscenarios, name="createescenario"),
    path("rotativos/deleteescenario/<int:id>/", views.deleteEscenarios, name="deleteescenario"),
    path("rotativos/updateescenario/<int:id>/", views.updateEscenarios, name="updateescenario"),
]
