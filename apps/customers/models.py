from django.db import models
from apps.plans.models import Plan, Activity

class Customer(models.Model):
    first_name = models.CharField("Nombre", max_length=100)
    last_name = models.CharField("Apellido", max_length=100)
    email = models.EmailField("Correo electrónico", unique=True)
    phone = models.CharField("Teléfono", max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pendiente'),
        ('paid', 'Pagado'),
        ('canceled', 'Cancelado'),
    ]
    booking_date = models.DateField("Fecha de reserva")
    status = models.CharField("Estado", max_length=10, choices=STATUS_CHOICES, default='pending')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="Cliente")
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, verbose_name="Plan")

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"
        ordering = ["-booking_date"]

    def __str__(self):
        return f"Reserva #{self.id} - {self.customer}"

class Payment(models.Model):
    amount = models.DecimalField("Monto", max_digits=10, decimal_places=2)
    payment_date = models.DateField("Fecha de pago")
    method = models.CharField("Método de pago", max_length=50)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, verbose_name="Reserva")

    class Meta:
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"
        ordering = ["-payment_date"]

    def __str__(self):
        return f"{self.method} - ${self.amount}"

class BookingActivity(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, verbose_name="Reserva")
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, verbose_name="Actividad")

    class Meta:
        verbose_name = "Actividad reservada"
        verbose_name_plural = "Actividades reservadas"
        unique_together = ('booking', 'activity')

    def __str__(self):
        return f"{self.activity} ({self.booking})"
