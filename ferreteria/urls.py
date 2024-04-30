from django.urls import path
from .views import index, compras, inise

urlpatterns = [
    path('', index, name='index'),
    path('compras/', compras, name='compras'),
    path('inise/',inise, name='inise'),
]