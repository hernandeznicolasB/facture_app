from django.urls import path
from . import views

urlpatterns = [
    path('', views.produit_list, name='produit_list'),
    path('creer/', views.produit_create, name='produit_create'),
    path('<int:pk>/modifier/', views.produit_edit, name='produit_edit'),
    path('<int:pk>/supprimer/', views.produit_delete, name='produit_delete'),
]
