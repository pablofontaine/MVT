from django.db import models

# Create your models here.

class Adventure(models.Model):
    place = models.CharField(max_length=40)
    date = models.DateField()

    def __str__(self) -> str:
        return f'Fecha {self.date} | Lugar {self.place}'