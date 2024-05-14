from django.urls import path
from django.contrib import admin
from .views import index, compras, inise, formularioRegistro, vista_bod
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index, name='index'),
    path('compras/', compras, name='compras'),
    path('inise/',inise, name='inise'),
    path('formularioRegistro/',formularioRegistro, name='formularioRegistro'),
    path('vista_bod/',vista_bod, name='vista_bod'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
]