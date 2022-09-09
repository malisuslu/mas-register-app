from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Student(models.Model):
    GENDER = [
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHER', 'Other'),
        ('NOT-TO-SAY', "Don't want to say"),
    ]
    PATH = [
        ('ENG', 'Engineering'),
        ('SS', 'Social Sciences'),
        ('ART', 'Arts'),
        ('OTHER', "Others"),
    ]
    
    full_name = models.CharField(max_length=50)
    number = models.IntegerField(null=False, blank=False, unique=True)
    mobile = PhoneNumberField(unique=True)
    email = models.EmailField(max_length=254, null=False, blank=False, unique=True)
    gender = models.CharField(max_length=20, null=False, choices=GENDER)
    path = models.CharField(max_length=20, null=False, choices=PATH)

    def __str__(self):
        return f"{self.id} - {self.full_name}"

    # def id_num(self):
    #     return f"{self.id}"

    class Meta:
        ordering = ["id"]