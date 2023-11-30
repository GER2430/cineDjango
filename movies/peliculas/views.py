from django.shortcuts import render
from .models import Pelicula
from .forms import addMovie
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Create your views here.
class listaPeliculas(ListView):
    model = Pelicula
    template_name = 'index.html'
    context_object_name = 'peliculas'
    success_url = 'peliculas'

class addPeliculas(CreateView):
    model = Pelicula
    template_name = 'new.html'
    context_object_name = 'peliculas'
    form_class = addMovie
    success_url = reverse_lazy('Listar')

class delPeliculas(DeleteView):
    model = Pelicula
    template_name = 'delete.html'
    success_url = reverse_lazy('Listar')

class upPeliculas(UpdateView):
    model = Pelicula
    template_name = 'new.html'
    context_object_name = 'peliculas'
    form_class = addMovie
    success_url = reverse_lazy('Listar')