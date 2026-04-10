from django.urls import path
from . import views

urlpatterns = [
    path('', views.facture_list, name='facture_list'),
    path('creer/', views.facture_create, name='facture_create'),
    path('<int:pk>/', views.facture_detail, name='facture_detail'),
    path('<int:pk>/supprimer/', views.facture_delete, name='facture_delete'),
]
