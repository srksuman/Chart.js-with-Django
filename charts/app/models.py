from django.db import models

# Create your models here.
class Student(models.Model):
    class_n = models.CharField(max_length=70)
    number_of = models.IntegerField()