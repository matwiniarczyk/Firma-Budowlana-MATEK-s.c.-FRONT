from django.db import models


class ProjectsDone(models.Model):
    title = models.CharField(max_length=100, default='')
    description = models.TextField(default='Brak opisu')
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)


class Services(models.Model):
    title = models.CharField(max_length=100, default='')
    description = models.TextField(default='Brak opisu')
    text = models.TextField(default='')
    image = models.ImageField(upload_to='images/', null=True, blank=True)
