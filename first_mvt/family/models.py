from django.db import models

# Create your models here.

class Family_member(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()
    relationship = models.CharField(max_length=40)

    def __str__(self):
        return f'Nombre: {self.name} | Apellido: {self.last_name} | Edad: {self.age} | Relación: {self.relationship}'

class Adventure(models.Model):
    place = models.CharField(max_length=40)
    date = models.DateField()

    def __str__(self) -> str:
        return f'Fecha {self.date} | Lugar {self.place}'

class Possession(models.Model):
    item = models.CharField(max_length=40)
    value = models.IntegerField()
    owner = models.CharField(max_length=40)

    def __str__(self) -> str:
        return f'Bien {self.item} vale {self.value} y es de {self.owner}'