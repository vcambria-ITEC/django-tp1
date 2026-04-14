from django.db import models

class Clima(models.Model):
    nombre_ciudad = models.CharField(max_length=100)
    fecha_y_hora = models.DateTimeField()
    temperatura = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.nombre_ciudad} - {self.fecha_y_hora}"