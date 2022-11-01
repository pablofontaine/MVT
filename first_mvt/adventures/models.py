from django.db import models
# from ckeditor.fields import RichTextField

# Create your models here.

class Adventure(models.Model):
    place = models.CharField(max_length=40)
    date = models.DateField()
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'Fecha {self.date} | Lugar {self.place}'