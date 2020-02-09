from django.contrib.auth.models import User
from django.db import models

class Location(models.Model):
  """
  tier field is used to to check if one area is within car travel
  longitude and latitude is the coordinates of a location.
  """
  name = models.CharField(max_length=50, null=False, blank=False)
  longitude = models.DecimalField(
    max_digits=13, decimal_places=8, 
    null=False, blank=False)
  latitude = models.DecimalField(
    max_digits=13, decimal_places=8, 
    null=False, blank=False)
  tier = models.PositiveSmallIntegerField(
    help_text='Defines the region of the city for fare computation.', 
    null=False, blank=False) 

  def __str__(self):
    return '%s' % (self.name,)

  def __unicode__(self):
    return '%s' % (self.name,)

class Vehicle(models.Model): 
  name = models.CharField(max_length=10, primary_key=True)

  def __str__(self):
    return '%s' % (self.name,)

  def __unicode__(self):
    return '%s' % (self.name,)
 
class Airport(models.Model):
  name = models.CharField(max_length=100, null=False, blank=False)
  location = models.ForeignKey(Location, on_delete=models.PROTECT)
  capacity = models.PositiveSmallIntegerField(null=False, blank=False) 

  def __str__(self):
    return '%s' % (self.name,)

  def __unicode__(self):
    return '%s' % (self.name,)

class Fare(models.Model):
  """
  For testing purposes will not add audit of who editted.
  """ 
  vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=False)
  fare_type = models.CharField(max_length=10, null=False, blank=False)
  price = models.DecimalField(
    max_digits=5, decimal_places=2, 
    null=False, blank=False)
  tstamp = models.DateField(auto_now=True) 

  def __str__(self):
    return '%s\t%s' % (self.vehicle,self.fare_type)

  def __unicode__(self):
    return '%s\t%s' % (self.vehicle,self.fare_type)


class FareFormula(models.Model):
  vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=False)
  formula = models.CharField(max_length=100, null=False, blank=False) 

  def __str__(self):
    return '%s' % (self.vehicle,)

  def __unicode__(self):
    return '%s' % (self.vehicle,)

class Hotel(models.Model):
  name = models.CharField(max_length=100, null=False, blank=False)
  room_name = models.CharField(max_length=100, null=False, blank=False)
  no_of_pax = models.PositiveSmallIntegerField(
    null=False, 
    default=0) 
  location = models.ForeignKey(Location, on_delete=models.PROTECT)
  start_date = models.DateField(null=False, blank=False) 
  end_date = models.DateField(null=False, blank=False) 
  price = models.DecimalField(
    max_digits=5, decimal_places=2, 
    null=False, blank=False)
  no_of_rooms = models.PositiveSmallIntegerField(
    null=False, 
    default=0) 

  def __str__(self):
    return '%s' % (self.name,)

  def __unicode__(self):
    return '%s' % (self.name,)
 
## Main Form Model

class TravelDetails(models.Model):
  COMPANY  = 'C'
  SELF = 'SF'

  MODE_OF_TRAVEL = [
    (COMPANY, 'Company'),
    (SELF, 'Self'),
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
  mode_of_travel = models.CharField(
    max_length=4,
    choices=MODE_OF_TRAVEL,
    default=COMPANY
    ) 
  airport_origin = models.ForeignKey(
    Airport,
    related_name='airport_origin',
    on_delete=models.PROTECT,
    null=True)
  airport_dest = models.ForeignKey(
    Airport,
    related_name='airport_dest',
    on_delete=models.PROTECT,
    null=True)
  hotel = models.ForeignKey(
    Hotel,
    on_delete=models.PROTECT,
    null=True)
  approver = models.ForeignKey(
    User, 
    related_name='approver',
    on_delete=models.PROTECT,
    null=True)
  back_and_forth = models.BooleanField(null=True,default=True)
  status = models.CharField(
    max_length=10,
    choices=STATUS,
    default=DRAFT,
    ) 
  approver_feedback = models.CharField(max_length=300, blank=True, null=True) 
