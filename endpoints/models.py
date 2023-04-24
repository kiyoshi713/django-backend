from django.db import models

class Cliente(models.Model):
    username = models.CharField(max_length=25,primary_key=True)
    password = models.CharField(max_length=25)

    def __str__(self):
        return self.username

