from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class travelDetails(models.Model):
  MODE_OF_TRAVEL = [
    (COMPANY, 'C'),
    (SELF, 'SF'),
    (SEMI, 'SI'),
  ]
  name = models.ForeignKey(User, on_delete=models.PROTECT)
  start_date = models.DateField(required=True) 
  end_date = models.DateField(required=True) 
  mode_of_travel = models.CharField(
    max_length=1,
    choices=MODE_OF_TRAVEL,
    default=COMPANY,
    ) 
