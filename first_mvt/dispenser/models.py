from django.db import models

# Create your models here.

class Dispenser(models.Model):
    serial_number = models.CharField(max_lenght=10)
    machine_type = models.CharField(max_lenght=10)
    brand = models.CharField(max_lenght=10)
    model = models.CharField(max_lenght=10)
    color = models.CharField(max_lenght=10)
    purchase = models.CharField(max_lenght=10)

    def __str__(self, serial_number: str, machine_type: str, brand: str, model: str, color: str, purchase: str):
        return f'''
        N° de serie: {self.serial_number}
        Tipo: {self.machine_type}
        Marca: {self.brand}
        Modelo: {self.model}
        Color: {self.color}
        Fecha de compra {self.purchase}
        '''