from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class UserExtend(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200, blank=False)
    gender = models.CharField(max_length=10, blank=True)
    dob = models.DateField(blank=True,null=True)
    emi = models.CharField(max_length=15, default="")
    subscription = models.IntegerField(default=0)
    subscription_date = models.DateField(default=datetime.date.today())
