from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=50, null=False)
    price = models.FloatField(max_length=20)
    image = models.ImageField(max_length=200)
    release_date = models.DateField(max_length=20)
    lte_exists = models.BooleanField(max_length=10)
    slug = models.SlugField(max_length = 200, unique=True)
    
