from django.db import models

class Categoriaa(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id categoria')
    nombreCategoriaa = models.CharField(max_length=50, verbose_name="Categoria")

    def __str__(self):
        return self.nombreCategoriaa


class Arte(models.Model):
    id_arte = models.IntegerField(primary_key= True, verbose_name= 'identificador de obra')
    nombre = models.CharField(max_length=50, verbose_name= 'Nombre de Obra')
    autor = models.CharField(max_length= 30, verbose_name= 'Autor')
    descripcion = models.CharField(max_length=50, null=True, blank=True, verbose_name= 'Descripcion de obra')
    categoriaa = models.ForeignKey(Categoriaa, on_delete=models.CASCADE )

    def __str__(self):
        return self.id_arte
        
    
