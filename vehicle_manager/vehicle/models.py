from django.db import models

# Create your models here.

class Vehicle(models.Model):

    name = models.CharField(max_length=100)
    
    TYPE_OPTIONS = (
        ('Economy','Economy'),
        ('SUV','SUV'),
        ('sedan','sedan'),
        ('Hatchback','Hatchback'),
        ('electric','electric'),
        ('Hybrid','Hybrid'),
        ('Sports car','Sports car'),
        ('Coupe','Coupe'),
        ('Utility','Utility')

    )

    type = models.CharField(max_length=200,choices=TYPE_OPTIONS,default='Economy')

    ENGINE_TYPES = (
        ('Inline','Inline'),
        ('v Engine','v Engine'),
        ('W Engine','W Engine'),
        ('OPOC','OPOC')
    )

    engine = models.CharField(max_length=100,choices=ENGINE_TYPES,default='v Engine')

    FUEL_OPTIONS = (
        ('PETROL','PETROL'),
        ('DIESEL','DIESEL'),
        ('CNG','CNG'),
        ('ELECTRIC','ELECTRIC')
    )

    fuel = models.CharField(max_length=100,choices=FUEL_OPTIONS,default='PETROL')

    date = models.DateField(auto_now_add=True)

    amount = models.FloatField()
