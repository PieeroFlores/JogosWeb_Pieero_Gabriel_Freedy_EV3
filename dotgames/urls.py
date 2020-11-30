from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('juego/', views.JuegoListView.as_view(), name='juego'),
    path('juego/<str:pk>', views.JuegoDetailView.as_view(), name='juego-detail'),
    path('autor/<int:pk>', views.AutorDetailView.as_view(), name='autor-detail'),
    path('autor/', views.AutorListView.as_view(), name='autor')
     
]


urlpatterns+=[
    path('autor/create/', views.AutorCreate.as_view(), name='autor_create'),
    path('autor/<int:pk>/update/', views.AutorUpdate.as_view(), name='autor_update'),
    path('autor/<int:pk>/delete/', views.AutorDelete.as_view(), name='autor_delete'),
    path('juego/create/', views.JuegoCreate.as_view(), name='juego_create'),
    path('juego/<str:pk>/update/', views.JuegoUpdate.as_view(), name='juego_update'),
    path('juego/<str:pk>/delete/', views.JuegoDelete.as_view(), name='juego_delete'),
    
]


