from django.db import models

# Create your models here.

class Personal(models.Model):
    """Model with information about ALL PEOPLE"""

    name = models.CharField(max_length=150)
    skills = models.TextField(default=None, blank=True, null=True)

    def __str__(self):
        return self.name

class Ability(models.Model):
    """Model with information about ALL ABILITIES AND THIER VALUES"""

    name = models.CharField(max_length=100)
    category = models.ForeignKey('Categories', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class Categories(models.Model):
    """Model with information about ALL ABILITIES CATEGORIES"""

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
