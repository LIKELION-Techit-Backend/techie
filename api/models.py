from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):    
  id = models.BigAutoField(primary_key=True)
  first_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=20)
  email = models.CharField(max_length=30)
  password = models.CharField(max_length=20)
  
class Team(models.Model):
  id = models.BigAutoField(primary_key=True)
  team_name = models.CharField(max_length=30)
