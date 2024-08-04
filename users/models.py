from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):

    PATIENT_TYPE_CHOICES = (
        ('P', 'Patient'),
        ('D', 'Doctor'),
        ('A', 'Admin'),
    )
    type = models.CharField(max_length=1, choices=PATIENT_TYPE_CHOICES, default='P')
    phone = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username

class Patient(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    age = models.IntegerField(blank=True, null=True)
    medical_history = models.TextField(blank=True, null=True)
    room_no = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

class Doctor(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    age = models.IntegerField(blank=True, null=True)
    specialization = models.CharField(max_length=100, blank=True, null=True)
    experience = models.IntegerField(blank=True, null=True)
    qualification = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username


