from django.urls import path
from . import views

urlpatterns = [
    path("cdats/", views.Cdat, name="cdats"),
    path("createcdat/", views.createCdat, name="createcdat"),
    path("cdats/updatecdat/<int:id>/", views.updatecdat, name="updatecdat"),
    path("deletecdat/<int:id>/", views.deletecdat, name="deletecdat"),
]
