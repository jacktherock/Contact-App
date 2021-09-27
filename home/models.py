from django.db import models

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=70)
    mobile_no = models.IntegerField()
    