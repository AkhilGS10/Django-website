from django.db import models

class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    dob = models.DateField()
    email = models.EmailField(unique=True)
    otp = models.CharField(max_length=6, blank=True, null=True)
    password = models.CharField(max_length=50, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    phone_no = models.CharField(max_length=15)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    hobbies = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
