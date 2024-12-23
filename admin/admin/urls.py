from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('account.urls')),
    path('', include('controls.urls')),
    path('', include('cdat.urls')),
    path('', include('cooviahorro.urls')),
    path('', include('credito.urls')),
    path('', include('descuentos_Credito.urls')),
    path('', include('rotativo.urls')),
    path("api-registros/", include("registros.urls")),
    path('', include('asesores.urls')),
    path("api/", include("registros.urls")),
    path('admin/', admin.site.urls),
]
