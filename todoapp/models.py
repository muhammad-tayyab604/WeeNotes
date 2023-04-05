from django.db import models

class Notes(models.Model):
    title = models.CharField(max_length=100)
    discription = models.TextField()

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    contactNo = models.IntegerField()
    message = models.TextField()
