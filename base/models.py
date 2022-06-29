from tkinter import image_names
from django.db import models

# Create your models here.

class Data(models.Model):
    sno=models.AutoField(primary_key=True)
    image_name= models.CharField(max_length=255)
    objects_detected = models.CharField(max_length=255)
    timestamp = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'{self.image_name}'
