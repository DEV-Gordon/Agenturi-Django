from django.db import models

class Destination(models.Model):
    name = models.CharField("Nombre", max_length=100)
    country = models.CharField("Pais", max_length=100, blank=True, null=True)
    city = models.CharField("Ciudad", max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "Destino"
        verbose_name_plural = "Destinos"
        ordering = ["country", "city"]

    def __str__(self):
        return f"{self.name} - {self.city}, {self.country}"

class Accommodation(models.Model):
    name = models.CharField("Nombre", max_length=100)
    type = models.CharField("Tipo", max_length=50, blank=True, null=True)
    address = models.CharField("Direccion", max_length=150, blank=True, null=True)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, verbose_name="Destino")

    class Meta:
        verbose_name = "Alojamiento"
        verbose_name_plural = "Alojamientos"
        ordering = ["destination", "name"]

    def __str__(self):
        return f"{self.name} ({self.destination})"

class Transport(models.Model):
    type = models.CharField("Tipo", max_length=50)
    company = models.CharField("Compañía", max_length=100)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, verbose_name="Destino")

    class Meta:
        verbose_name = "Transporte"
        verbose_name_plural = "Transportes"
        ordering = ["destination", "type"]

    def __str__(self):
        return f"{self.type} - {self.company}"