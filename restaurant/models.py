from django.db import models

# Create your models here.
class Menu(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)    
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return self.title

class Booking(models.Model):
    id= models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    guests = models.IntegerField()
    booking_date = models.DateTimeField()

    def __str__(self):
        return self.name