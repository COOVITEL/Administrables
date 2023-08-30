from django.urls import path
from . import views

urlpatterns = [
    path("", views.Index, name="index"),
    path("register", views.Register, name="register"),
    path("login", views.login, name="login"),
    path("user-logout", views.user_logout, name="user-logout"),
    path("cdats", views.Cdat, name="cdats"),
    path("cooviahorro", views.Cooviahorro, name="cooviahorro"),
    path("administrables", views.Admin, name="admin")
]