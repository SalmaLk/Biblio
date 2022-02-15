from distutils.command.upload import upload
from pickle import TRUE
from random import choices
from turtle import title
from unicodedata import name
from django.db import models

# Create your models here.
class Category(models.Model):
    id = models.IntegerField
    name = models.CharField(max_length= 50)
    def __str__(self):
        return self.name

class Book(models.Model):
    status_book = [
        ('available', 'available'),
        ('rental', 'rental'),
        ('sold', 'sold'),
    ] 
    id = models.IntegerField
    title = models.CharField(max_length= 250)
    author =  models.CharField(max_length= 250)
    photo_book = models.ImageField(upload_to = 'photos', null = TRUE, blank = TRUE)
    photo_author =  models.ImageField(upload_to = 'photos', null = TRUE, blank = TRUE)
    pages = models.IntegerField(null = TRUE, blank = TRUE)
    price = models.DecimalField(max_digits= 10, decimal_places= 2, null = TRUE, blank = TRUE)
    rental_price_day = models.DecimalField(max_digits= 5, decimal_places= 2, null = TRUE, blank = TRUE)
    total_rental =  models.DecimalField(max_digits= 5, decimal_places= 2, null = TRUE, blank = TRUE)
    rental_period = models.IntegerField(null = TRUE, blank = TRUE)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=50, choices= status_book, null = TRUE, blank = TRUE)
    category = models.ForeignKey(Category, on_delete= models.PROTECT, null = TRUE, blank = TRUE)


    def __str__(self):
        return self.title
class User (models.Model):
    userName = models.CharField(max_length= 250)
    login =  models.IntegerField

    def __str__(self):
        return self.userName

class author(models.Model):
    author_id = models.IntegerField
    author_name = models.CharField(max_length= 250)
    def __str__(self):
        return self.author_name
