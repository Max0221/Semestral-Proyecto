from django.urls  import path
from rest.views import lista_Obras

urlpatterns = [
    path('Artes', lista_Obras, name="lista_Obras"),
]