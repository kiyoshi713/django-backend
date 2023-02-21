from django.contrib import admin
from . import models


# Register your models here.
admin.site.register(models.Cliente)
admin.site.register(models.Restaurant_Cat)
admin.site.register(models.Restaurant)
admin.site.register(models.Categoria_Plato)
admin.site.register(models.Plato)
admin.site.register(models.Form)
admin.site.register(models.Menu)