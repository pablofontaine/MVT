from django.db import models

# Create your models here.


class Possession(models.Model):
    item = models.CharField(max_length=40)
    value = models.IntegerField()
    owner = models.CharField(max_length=40)

    def __str__(self) -> str:
        return f'Bien {self.item} vale {self.value} y es de {self.owner}'