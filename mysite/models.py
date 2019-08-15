from django.db import models

# Create your models here.

class Person(models.Model):
    first_name=models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name + "  " + self.last_name


class Contact(models.Model):
    email=models.EmailField()
    subject=models.CharField(max_length=200)
    message=models.TextField()

    def __str__(self):
        return self.email



