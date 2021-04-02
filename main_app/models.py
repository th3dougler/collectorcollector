from django.db import models
from django.urls import reverse

COLOURS = (
    ('0', 'White'),
    ('1', 'Black'),
    ('2', 'Red'),
    ('3', 'Orange'),
    ('4', 'Yellow'),
    ('5', 'Green'),
    ('6', 'Blue'),
    ('7', 'Indigo'),
    ('8', 'Violet'),
)

class Collector(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    capacity = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('collector-detail', kwargs={'pk': self.id} )
    
class WhatGoesIn(models.Model):
    name = models.CharField(max_length=100)
    colour = models.CharField(max_length=1,
                              choices=COLOURS,
                              default=COLOURS[2][0])
    collector = models.ForeignKey(Collector, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    