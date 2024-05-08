from django.urls import path
from .views import index, compras, inise, registrar

urlpatterns = [
    path('', index, name='index'),
    path('compras/', compras, name='compras'),
    path('inise/',inise, name='inise'),
    path('registrar/',registrar, name='registrar'),
]