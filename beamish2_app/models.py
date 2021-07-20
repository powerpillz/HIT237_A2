from django.db import models

# Create your models here.


class Minerals(models.Model):
    mineral_name = models.CharField(max_length=25, unique=True)
    symbol = models.CharField(max_length=3)
    atomic_num = models.PositiveIntegerField(default=0)
    appearance = models.CharField(max_length=25)
    description = models.TextField(default='Enter Fun Facts Here!')


    def __str__(self):
        return self.mineral_name

class Company(models.Model):
    company_name = models.CharField(max_length=50)
    asx_code = models.CharField(max_length=8, default="ASX")
    website = models.URLField()
    chief_officer = models.CharField(max_length=50)
    mineral_profile = models.ManyToManyField(Minerals)

    def __str__(self):
        return self.company_name

#Principle Topic
class Minesite(models.Model):
    site_name = models.CharField(max_length=50)
    owners = models.ManyToManyField(Company)
    location = models.CharField(max_length=25)
    region = models.CharField(max_length=25)
    minerals = models.ManyToManyField(Minerals)
    production = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.id) + ": " + self.site_name
