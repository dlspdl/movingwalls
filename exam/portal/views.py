import re

from datetime import datetime as dt
from geopy.distance import geodesic

from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView

from portal.forms import TravelForm
from portal.models import Airport, Hotel, Fare 
from portal.models import FareFormula, Location, TravelDetails

def check_airport(origin, hotel, airport_origin, airport_dest):
  if airport_origin == airport_dest:
    response = "Cannot book same airport"
    return response
  elif airport_origin.location.tier != origin.tier:
    response = "Origin and airport origin must be at the same tier."
    return response
  elif airport_dest.location.tier != hotel.location.tier:
    response = "Hotel and airport dest must be at the same tier."
    return response 
  return None

def comp_with_plane(objects):
  origin = objects.origin
  hotel = objects.hotel
  airport_origin = objects.airport_origin
  airport_dest = objects.airport_dest

  origin_coordinates = (origin.latitude,origin.longitude)    
  hotel_coordinates = (hotel.location.latitude,hotel.location.longitude)    
  ao_coordinates = (ao.location.latitude,ao.location.longitude)    
  ad_coordinates = (ad.location.latitude,ad.location.longitude)    

  distance1 = geodesic(origin_coordinates, ao_coordinates).km
  distance2 = geodesic(ad_coordinates, hotel_coordinates).km
  distance3 = geodesic(ao_coordinates, ad_coordinates).km

  car_fare = Fare.objects.filter(vehicle='car')
  car_formula = FareFormula.objects.get(vehicle='car')
  car1 = re.sub('KM', str(distance1), car_formula.formula)
  car2 = re.sub('KM', str(distance2), car_formula.formula)

  for fare in car_fare:
    car1 = re.sub(fare.fare_type, str(round(fare.price,2)), car1)
    car2 = re.sub(fare.fare_type, str(round(fare.price,2)), car2)

  plane_fare = Fare.objects.filter(vehicle='plane')
  plane_formula = FareFormula.objects.get(vehicle='plane')
  plane = re.sub('KM', str(distance3), plane_formula.formula)

  for fare in plane_fare:
    plane1 = re.sub(fare.fare_type, str(round(fare.price,2)), plane1)

#  car_fare = Fare.objects.filter(vehicle='car')
#  car_formula = FareFormula.objects.get(vehicle='car').values('formula')

def comp_wout_plane(objects):
  plane_fare = 0
  origin = objects.origin
  hotel = objects.hotel

  origin_coordinates = (origin.latitude,origin.longitude)    
  hotel_coordinates = (hotel.location.latitude,hotel.location.longitude)    
  distance = geodesic(origin_coordinates, hotel_coordinates).km
  
  car_fare = Fare.objects.filter(vehicle='car')
  car_formula = FareFormula.objects.get(vehicle='car')
  car_formula = re.sub('KM', str(distance), car_formula.formula)
  
  for fare in car_fare:
    car_formula = re.sub(fare.fare_type, str(round(fare.price,2)), car_formula)

  car_formula = re.sub(' ', '', car_formula)
  objects.car_formula = car_formula 

  return objects
   
def validator(objects):
  w_plane = 0
  start_date = objects.start_date
  end_date = objects.end_date
  
  if start_date >= end_date:
    response = "Error: Start Date later than End Date."
    return response, objects

  origin = objects.origin
  hotel = objects.hotel
  airport_origin = objects.airport_origin if hasattr(objects, 'airport_origin') else None
  airport_dest = objects.airport_dest if hasattr(objects, 'airport_dest') else None
  
  if origin.tier != hotel.location.tier:
    if airport_origin == None or airport_dest == None:
      response = origin.name + " is not on the same region as " + hotel.location.name + " must book a flight."
      return response, objects, 0
    w_plane = 1
  else:
    if airport_origin != None or airport_dest != None:
      response = check_airport(origin. hotel, airport_origin, airport_dest)
      if response is None:
        return response, objects, 0 
      w_plane = 1
        
  response = "Success"
  return response, objects, w_plane

class TraverlInsertView(CreateView):
  model = TravelDetails
  form_class = TravelForm
  template_name = settings.BASE_DIR + '/portal/templates/travel_form.html'
  
  def form_valid(self, form):
    self.object = form.save(commit = False)
    storage = messages.get_messages(self.request)
    storage.used = True
    self.object.name = self.request.user 

    #Validator
    response, objects, w_plane = validator(self.object)

    if response != "Success":
      messages.add_message(self.request, messages.ERROR, response)
      return HttpResponseRedirect(reverse('travelform'))
    else:
      #Success
      objects = comp_with_plane(objects) if w_plane == 1 else comp_wout_plane(objects)
      self.object = objects
      messages.add_message(self.request, messages.INFO, 'Success.')
      self.object.save()
      return HttpResponseRedirect(reverse('travelform'))
  
    
