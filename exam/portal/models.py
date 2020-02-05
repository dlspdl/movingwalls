from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class TravelDetails(models.Model):
  COMPANY  = 'C'
  SELF = 'SF'
  SEMI = 'SI'

  MODE_OF_TRAVEL = [
    (COMPANY, 'Company'),
    (SELF, 'Self'),
    (SEMI, 'Semi'),
  ]

  DRAFT = 'DRAFT'
  SUBMITTED = 'SUBMITTED'
  REJECTED = 'REJECTED'
  APPROVED = 'APPROVED'
  REQUEST_FOR_INFO = 'RFI'
  
  STATUS = [ 
    (DRAFT, 'Draft'),
    (SUBMITTED, 'Submitted'),
    (REJECTED, 'Rejected'),
    (APPROVED, 'Approved'),
    (REQUEST_FOR_INFO, 'Request for Information'),
  ] 

  name = models.ForeignKey(
    User, 
    related_name='requestor',
    on_delete=models.PROTECT)
  start_date = models.DateField(null=False, blank=False) 
  end_date = models.DateField(null=False, blank=False) 
  desc = models.CharField(max_length=300, blank=True, null=True) 
  approver_feedback = models.CharField(max_length=300, blank=True, null=True) 
  mode_of_travel = models.CharField(
    max_length=4,
    choices=MODE_OF_TRAVEL,
    default=COMPANY,
    ) 
  approver = models.ForeignKey(
    User, 
    related_name='approver',
    on_delete=models.PROTECT,
    null=True)
  status = models.CharField(
    max_length=10,
    choices=STATUS,
    default=DRAFT,
    ) 

class BaseFare(models.Model):
  """
  For testing purposes will not add audit of who editted.
  """
  fare_type = models.CharField(max_length=10, null=False, blank=False)
  price = models.DecimalField(
    max_digits=5, decimal_places=2, 
    null=False, blank=False)
  tstamp = models.DateField(auto_now=True) 

#  def save(self, *args, **kwargs):
#    if not self._state.adding:
#      
#    super().save(*args, **kwargs)

class BaseFareHist(models.Model):
  fare_type = models.CharField(max_length=10, null=False, blank=False)
  price = models.DecimalField(
    max_digits=5, decimal_places=2, 
    null=False, blank=False)
  start_date = models.DateField(null=False, blank=False) 
  end_date = models.DateField(null=False, blank=False) 
 
class Location(models.Model):
  """
  tier field is used to to check if one area is within car travel
  longitude and latitude is the coordinates of a location.
  """
  name = models.CharField(max_length=50, null=False, blank=False)
  tier = models.PositiveSmallIntegerField(
    help_text='Defines the region of the city for fare computation.', 
    null=False, blank=False) 
  longitude = models.DecimalField(
    max_digits=4, decimal_places=4, 
    null=False, blank=False)
  latitude = models.DecimalField(
    max_digits=4, decimal_places=4, 
    null=False, blank=False)

class HotelDetails(models.Model):
  name = models.CharField(max_length=100, null=False, blank=False)
  location = models.ForeignKey(Location, on_delete=models.PROTECT)
  start_date = models.DateField(null=False, blank=False) 
  end_date = models.DateField(null=False, blank=False) 
  price = models.DecimalField(
    max_digits=5, decimal_places=2, 
    null=False, blank=False)
