from datetime import datetime as dt

from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView

from portal.forms import TravelForm
from portal.models import Airport, Hotel, Fare 
from portal.models import FareFormula, Location, TravelDetails

class TraverlInsertView(CreateView):
  model = TravelDetails
  form_class = TravelForm
  template_name = settings.BASE_DIR + '/portal/templates/travel_form.html'
  
  def form_valid(self, form):
    self.object = form.save(commit = False)
    self.object.name = self.request.user 

    #Validator
    response, objects = validator(self.object)

    #Success
    self.object = objects
    messages.add_message(self.request, messages.INFO, 'Success.')
    self.object.save()
    return HttpResponseRedirect(reverse('travelform'))
  
  def validator(objects):
    start_date = dt.strptime(objects.start_date,"%Y-%m-%d")
    end_date = dt.strptime(objects.end_date,"%Y-%m-%d")
    
    if start_date >= end_date:
      response = "Error: Start Date later than End Date."
      return response, objects

    origin = objects.origin
    hotel = objects.hotel
    airplane_origin = objects.airplane_origin
    airplane_dest = objects.airplane_dest
    
    if origin != hotel.location and ( not airplane_origin or not airplane_dest ):
      response = origin.name + "is not on the same region as " + hotel.location.name + "must book a flight."
      return response, objects

    response = "Success"
    return response, objects
    
