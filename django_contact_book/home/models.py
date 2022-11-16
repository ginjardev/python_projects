from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField()
    contact_number = models.CharField(max_length=11)