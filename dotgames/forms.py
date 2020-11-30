from django import forms
from .models import Juego, Genero, Autor



class JuegoForm(forms.ModelForm):
    titulo = forms.CharField(label='Titulo',max_length=100, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    descripcion = forms.CharField(label='Descripción', max_length=1000, widget=forms.Textarea(
        attrs={
            'class':'form-control'
        }
    ))
   
    genero = forms.ModelChoiceField(queryset=Genero.objects.all(), label='Género',
            widget=forms.Select(
            attrs={
                'class':'form-control' 
            }
            ))

    autor = forms.ModelChoiceField(queryset=Autor.objects.all(), label='Autor',
            widget=forms.Select(
            attrs={
                'class':'form-control' 
            }
            ))
    portada = forms.ImageField(label='Imagen',
            widget=forms.ClearableFileInput(
            attrs={
                'class':'form-control' 
            }
            ))

             
    class Meta:
        model = Juego
        fields = ('titulo','descripcion', 'portada', 'autor', 'genero' )