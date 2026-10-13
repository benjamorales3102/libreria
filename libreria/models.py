from django.db import models


class editorial(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField(blank=True)

    def __str__(self):
        return self.nombre


class libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    editorial = models.ForeignKey(editorial, on_delete=models.CASCADE)
    fecha_publicacion = models.DateField()
    isbn = models.CharField(max_length=13)
    precio = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True, null=True)

    @property
    def precio_formateado(self):
        if self.precio is None:
            return "Sin precio"
        return f"${self.precio:,.0f}".replace(",", ".")

    def __str__(self):
        return self.titulo