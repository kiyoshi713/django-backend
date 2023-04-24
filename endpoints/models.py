from django.db import models

class Usuario(models.Model):
    username = models.CharField(max_length=25,primary_key=True)
    password = models.CharField(max_length=25)

    def __str__(self):
        return self.username

