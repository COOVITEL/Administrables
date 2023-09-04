from django.urls import path
from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path("user-logout", views.user_logout, name="user-logout"),
    path("cdats", views.Cdat, name="cdats"),
    path("createcdat", views.createCdat, name="createcdat"),
    path("cdats/updatecdat/<int:id>", views.updatecdat, name="updatecdat"),
    path("deletecdat/<int:id>", views.deletecdat, name="deletecdat"),
    path("cooviahorro", views.Cooviahorro, name="cooviahorro"),
    path("createcooviahorro", views.createCooviahorro, name="createcooviahorro"),
    path("cooviahorro/update/<int:id>", views.updatecooviahorro, name="updatecooviahorro"),
    path("deletecooviahorro/<int:id>", views.deletecooviahorro, name="deletecooviahorro"),
    path("cooviahorro/updatecooviahorro/<int:id>", views.updatecooviahorro, name="updatecooviahorro"),
    path("administrables", views.Admin, name="admin"),
]