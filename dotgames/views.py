from django.shortcuts import render, redirect, get_object_or_404
from . models import Juego, Genero, Autor
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . forms import JuegoForm

def index(request):
    num_juegos=Juego.objects.all()
    return render(request, 'index.html', 
    context={'num_juegos':num_juegos},)

def juegos(request):
    num_juegos=Juego.objects.all()
    
    return render(
        request,
        'juegos.html',
        context={'num_juegos':num_juegos},
    )

class JuegoListView(generic.ListView):
    model = Juego
    paginate_by = 10
class JuegoDetailView(generic.DetailView):
    model = Juego

class AutorCreate(CreateView):

    def form_valid(self, form):
        form.instance.nombre=self.request.user
        return super().form_valid(form)


    model = Autor
    fields = '__all__'
    initial ={'nombre': ''}
    success_url = reverse_lazy('index')

class AutorUpdate(UpdateView):
   
    model = Autor
    fields = ['sexo','descripcion','foto']

class AutorDelete(DeleteView):
    model = Autor
    success_url = reverse_lazy('autor')


class AutorDetailView(generic.DetailView):
    model=Autor

class AutorListView(generic.ListView):
    model = Autor
    paginate_by = 10

class JuegoCreate(CreateView):
    model = Juego
    fields = '__all__'
    initial ={'titulo': ''}

class JuegoUpdate(UpdateView):
    model = Juego
    fields = ['titulo']


class JuegoDelete(DeleteView):
    model = Juego
    success_url = reverse_lazy('juego')

def Juego_new(request):
    if request.method == "POST":
        form = JuegoForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            #form.save_m2m()
            return redirect('juego-detail', pk=post.pk)
    else:
        form = JuegoForm()
        return render(request, 'spacedot/juego_form.html', {'form': form})

def Juego_edit(request, pk):
    post = get_object_or_404(Juego, pk=pk)
    if request.method == "POST":
        form = JuegoForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('juego-detail', pk=post.pk)
    else:
        form = JuegoForm(instance=post)
    return render(request, 'spacedot/juego_form.html', {'form': form})