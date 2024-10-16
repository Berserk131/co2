from django.db import models

class ProductoTecnologico(models.Model):
    nombre = models.CharField(max_length=200)
    material = models.CharField(max_length=200)
    energia_utilizada = models.CharField(max_length=100)  # Tipo de energía utilizada
    obsolescencia = models.IntegerField()  # Años de vida útil estimada
    pais_productor = models.CharField(max_length=100)
    huella_carbono = models.FloatField()  # Valor de la huella de carbono calculado

    def __str__(self):
        return self.nombre
