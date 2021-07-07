from django.db import models

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name="Categoria")

    def __str__(self):
        return self.nombreCategoria 


class Obra(models.Model):
    id_obra = models.IntegerField(primary_key= True, max_length=6 , verbose_name= 'identificador de obra')
    nombre = models.CharField(max_length=50, verbose_name= 'Nombre de Obra')
    autor = models.CharField(max_length= 30, verbose_name= 'Autor')
    descripcion = models.CharField(max_length=50, null=True, blank=True, verbose_name= 'Descripcion de obra')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE )

    def __str__(self):
        return self.id_obra
    
