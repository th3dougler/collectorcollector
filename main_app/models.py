from django.db import models
from django.urls import reverse

class Collector(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    capacity = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('collector-detail', kwargs={'pk': self.id} )
    
