from turtle import title
from django.db import models

# Create your models here.

class Book(models.Model):
  title = models.CharField(max_length=100) # sql knows book will have title field with some text
  rating = models.IntegerField()
  # including field below is not necessary, DJANGO automatically does this
  # id = models.AutoField() 

