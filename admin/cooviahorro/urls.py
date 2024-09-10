from django.urls import path
from . import views

urlpatterns = [
    path("cooviahorro/", views.Cooviahorro, name="cooviahorro"),
    path("createcooviahorro/", views.createCooviahorro, name="createcooviahorro"),
    path("deletecooviahorro/<int:id>/", views.deletecooviahorro, name="deletecooviahorro"),
    path("cooviahorro/updatecooviahorro/<int:id>/", views.updatecooviahorro, name="updatecooviahorro"),
]
