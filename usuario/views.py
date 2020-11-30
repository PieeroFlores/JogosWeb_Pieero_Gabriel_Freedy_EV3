from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

class Registro(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('autor_create')
    template_name = 'registro.html'