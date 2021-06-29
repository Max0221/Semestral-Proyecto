from django.urls import path
from .views import index, contacto, login, artista, categoria, formulario, listap, recuperar, registro,compraVenta

urlpatterns = [
    path('',index, name="index"),
    path('contacto/', contacto, name="contacto"),
    path('login/', login, name="login"),
    path('artista/', artista, name="artista"),
    path('categoria/', categoria, name="categoria"),
    path('formulario/', formulario, name="formulario"),
    path('listap/', listap, name="listap"),
    path('recuperar/', recuperar, name="recuperar"),
    path('registro/', registro, name="registro"),
    path('compraVenta/', compraVenta, name="compraVenta")
    

]