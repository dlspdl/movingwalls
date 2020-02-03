from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class travelDetails(models.Model):
  COMPANY  = 'C'
  SELF = 'SF'
  SEMI = 'SI'
  MODE_OF_TRAVEL = [
    (COMPANY, 'Company'),
    (SELF, 'Self'),
    (SEMI, 'Semi'),
  ]
  name = models.ForeignKey(User, on_delete=models.PROTECT)
  start_date = models.DateField(null=False,blank=False) 
  end_date = models.DateField(null=False,blank=False) 
  mode_of_travel = models.CharField(
    max_length=4,
    choices=MODE_OF_TRAVEL,
    default=COMPANY,
    ) 
