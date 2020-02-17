from datetime import datetime as dt

from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, ListView

from portal import functions as fc
from portal.forms import TravelInsertForm
from portal.models import Airport, Hotel, Fare 
from portal.models import FareFormula, Location, TravelDetails

class TravelInsertView(LoginRequiredMixin, CreateView):
  model = TravelDetails
  form_class = TravelInsertForm
  template_name = settings.BASE_DIR + '/portal/templates/travel_form.html'
  
  def form_valid(self, form):
    self.object = form.save(commit = False)
    storage = messages.get_messages(self.request)
    storage.used = True
    self.object.name = self.request.user 

    #Validator
    response, objects, w_plane = fc.validator(self.object)

    if response != "Success":
      messages.add_message(self.request, messages.ERROR, response)
      return HttpResponseRedirect(reverse('travelform'))
    else:
      #Success
      objects = fc.comp_with_plane(objects) if w_plane == 1 else fc.comp_wout_plane(objects)
      self.object = objects
      messages.add_message(self.request, messages.INFO, 'Success.')
      self.object.save()
      return HttpResponseRedirect(reverse('travelform'))
  
class TravelView(LoginRequiredMixin, ListView): 
  model = TravelDetails
  template_name = settings.BASE_DIR + '/portal/templates/travel_view.html'
  context_object_name = 'travel_details'

  def get_queryset(self):
    queryset = super(TravelView, self).get_queryset()
    return queryset.filter(name=self.request.user)

