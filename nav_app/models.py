from django.db import models

# Create your models here.
class table(models.Model):
    name=models.CharField(max_length=30)
    Email=models.EmailField(max_length=40)
    Number=models.IntegerField(max_length=10)
    Date=models.DateField()
    Person=models.IntegerField(max_length=2)
