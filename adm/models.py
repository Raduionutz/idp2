from django.db import models

# Create your models here.

class Produs(models.Model):
    nume = models.CharField(max_length=256)
    pret = models.FloatField(default=1000.56)
    descriere = models.CharField(max_length=4096, default='Nu exista descriere')

    def __str__(self):
        return self.nume
