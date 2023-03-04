from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Task(models.Model):

    COLOR_CHOICES = [
        ('primary', 'Azul'),
        ('secondary', 'Gris'),
        ('success', 'Verde'),
        ('danger', 'Rojo'),
        ('warning', 'Amarillo'),
        ('info', 'Azul claro'),
        ('light', 'Blanco'),
        ('dark', 'Negro'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateField(auto_now=True)
    limite_date = models.DateField()
    status = models.BooleanField(default=False)
    color = models.CharField(max_length=20, choices=COLOR_CHOICES, default='primary' )


    def __str__(self) -> str:
        return self.title