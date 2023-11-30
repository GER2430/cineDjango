from django import forms
from .models import Pelicula

class addMovie(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = '__all__'