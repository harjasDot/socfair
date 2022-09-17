from django.db import models

# Create your models here.
class QUESTION(models.Model):
    name=models.CharField(blank=False,max_length=50)
    q1=models.CharField(blank=False,max_length=900)
    q2=models.CharField(blank=False,max_length=900)
    q3=models.CharField(blank=False,max_length=900)


    def __str__(self):
        return f"{self.name}, {self.q2}"