from django.db import models


class Ciudad(models.Model):
    nombre_ciudad = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_ciudad

class Clima(models.Model):
    ciudad = models.ForeignKey(
        Ciudad,
        on_delete=models.CASCADE,
        related_name="ciudad",
        default=None,
        blank=False,
        null=False
    )
    fecha_y_hora = models.DateTimeField()
    temperatura = models.DecimalField(max_digits=5, decimal_places=2)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.ciudad.nombre_ciudad} - {self.fecha_y_hora}"