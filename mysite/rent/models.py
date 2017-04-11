from django.db import models

# Create your models here.


class InventoryItem(models.Model):
    name = models.CharField(max_length=10)
    quantity = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.name