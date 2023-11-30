from django.urls import path
from .views import listaPeliculas, addPeliculas, delPeliculas, upPeliculas

urlpatterns = [
    path('', listaPeliculas.as_view(), name='Listar'),
    path('addPelicula/', addPeliculas.as_view(), name='Añadir'),
    path('delPelicula/<int:pk>', delPeliculas.as_view(), name='Borrar'),
    path('actPelicula/<int:pk>', upPeliculas.as_view(), name='actualizar'),]