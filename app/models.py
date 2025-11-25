from django.db import models
from django.contrib.auth.models import User

class Station(models.Model):
    name = models.CharField(max_length=100)
    line = models.CharField(max_length=50)
    neighbors = models.ManyToManyField("self", symmetrical=True, blank=True)

class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start = models.ForeignKey(Station, related_name='start', on_delete=models.CASCADE)
    status = models.CharField(max_length=20)