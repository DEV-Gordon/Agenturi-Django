from django.db import models
from apps.destination.models import Destination

class Plan(models.Model):
    name = models.CharField("Nombre", max_length=100)
    description = models.TextField("Descripción", blank=True, null=True)
    base_price = models.DecimalField("Precio base", max_digits=10, decimal_places=2)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, verbose_name="Destino")

    class Meta:
        verbose_name = "Plan"
        verbose_name_plural = "Planes"
        ordering = ["name"]

    def __str__(self):
        return self.name

class Itinerary(models.Model):
    day = models.IntegerField("Día")
    description = models.TextField("Descripción", blank=True, null=True)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, verbose_name="Plan")

    class Meta:
        verbose_name = "Itinerario"
        verbose_name_plural = "Itinerarios"
        ordering = ["plan", "day"]

    def __str__(self):
        return f"Día {self.day} - {self.plan.name}"

class Activity(models.Model):
    name = models.CharField("Nombre", max_length=100)
    description = models.TextField("Descripción", blank=True, null=True)
    extra_cost = models.DecimalField("Costo extra", max_digits=10, decimal_places=2, default=0)
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE, verbose_name="Itinerario")

    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"
        ordering = ["itinerary", "name"]

    def __str__(self):
        return self.name

class Guide(models.Model):
    name = models.CharField("Nombre", max_length=100)
    phone = models.CharField("Teléfono", max_length=20)
    language = models.CharField("Idioma", max_length=50)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, verbose_name="Plan")

    class Meta:
        verbose_name = "Guía"
        verbose_name_plural = "Guías"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.language})"
