from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
  username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
  email = models.EmailField(unique = True)
  phone_no = models.CharField(max_length = 10)
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
  def __str__(self):
      return "{}".format(self.email)
  

class Studentdata(models.Model):
  Date = models.CharField(max_length=255)
  Name = models.CharField(max_length=255)
  Father_name = models.CharField(max_length=255)
  College = models.CharField(max_length=255)
  Phone = models.CharField(max_length=255)
  Alternate_phone = models.CharField(max_length=255)
  Paid_Amount = models.CharField(max_length=255)
  Mode_of_payment = models.CharField(max_length=255)
  Balance_amount = models.CharField(max_length=255)
  Type_of_course = models.CharField(max_length=255)
  Cources_name = models.CharField(max_length=255)
  additional_course = models.CharField(max_length=255)