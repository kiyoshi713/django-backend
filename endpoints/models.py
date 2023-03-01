from django.db import models

class Cliente(models.Model):
    username = models.CharField(max_length=25,primary_key=True)
    password = models.CharField(max_length=25)

    def __str__(self):
        return self.username

class Restaurant_Cat(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Restaurant(models.Model):
    restaurant_estado=(("A","activo"),("I","inactivo"))
    usuario = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    nombre = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=500)
    logo = models.CharField(max_length=100)
    categoria_Rest = models.ForeignKey(Restaurant_Cat, on_delete=models.CASCADE, null= False)
    estado=models.CharField(max_length=1,choices=restaurant_estado)
    def __str__(self):
        return self.nombre

class Categoria_Plato(models.Model):
    
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Plato(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(decimal_places=2, max_digits=4)
    img = models.URLField()
    dscr = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria_Plato , on_delete=models.CASCADE,null=False)
    restaurante = models.ForeignKey(Restaurant,on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.nombre

class Form(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=False)
    rest = models.CharField(max_length=100)
    valoracion=models.CharField(max_length=2)
    comentario = models.CharField(max_length=250)
    
    def __str__(self):
        return self.nombre

class CategoriasporRestaurante(models.Model):
    categoria = models.ForeignKey(Categoria_Plato,on_delete=models.CASCADE,null=False)
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE,null=False)

class orden(models.Model):
    usuario=models.ForeignKey(Cliente,on_delete=models.CASCADE,null=False)
    monto=models.DecimalField(decimal_places=2,max_digits=5)
    direccion=models.CharField(max_length=40)
    fecha=models.CharField(max_length=10)
    estado=models.CharField(max_length=10)
    def __str__(self):
        return self.usuario