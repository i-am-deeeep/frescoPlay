from django.db import models

# Create your models here.
class Item(models.Model):
    name=models.CharField(max_length=40)
    category=models.CharField(max_length=40)
    price=models.IntegerField()
    quantity=models.IntegerField()
    barcode=models.IntegerField(unique=True)
