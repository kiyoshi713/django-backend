from django.db import models

class Platos(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    precio = models.DecimalField(decimal_places=2, max_digits=4)
    img = models.URLField()
    dscr = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
