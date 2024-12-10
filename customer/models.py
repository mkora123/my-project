from django.db import models

# Create your models here.
class Customer(models.Model):
    image = models.ImageField(upload_to='customer_images/',blank=True)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=25)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Appointment(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=25)
    phone = models.CharField(max_length=11)
    appointment_date = models.DateField()
    appointment_time = models.CharField(max_length=15)
    notes = models.TextField()

    def __str__(self):
        return self.name














class Doctor(models.Model):
    image = models.ImageField(upload_to='doctor_images/',blank=True)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=25)
    speciality = models.CharField(max_length=20)

    def __str__(self):
        return self.name



class MyUser(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username

