""" Define los patrones URL para users. """

from django.urls import path, include

app_name = "urls"
urlpatterns = [
    # Incluye las urls de auth default.
    path('', include('django.contrib.auth.urls')),
]