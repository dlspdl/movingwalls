from datetime import datetime as dt

from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView

from portal import functions as fc
from portal.forms import TravelInsertForm
from portal.models import Airport, Hotel, Fare 
from portal.models import FareFormula, Location, TravelDetails

class TravelInsertView(LoginRequiredMixin, CreateView):
  model = TravelDetails
  form_class = TravelInsertForm
  template_name = settings.BASE_DIR + '/portal/templates/travel_form.html'

  def get_form_kwargs(self):
    kwargs = super().get_form_kwargs()
    kwargs['user'] = self.request.user
    return kwargs
 
  def form_valid(self, form):
    self.object = form.save(commit = False)
    storage = messages.get_messages(self.request)
    storage.used = True
    self.object.name = self.request.user 

    if 'submit' in self.request.POST and self.request.POST["submit"] == "Submit":
      self.object.status = "SUBMITTED"

    if self.request.user.groups.filter(name__in=["MANAGER","F_MANAGER"]).exists():
      return HttpResponseRedirect(reverse('home'))

    #Validator
    response, objects, w_plane = fc.validator(self.object)

    if response != "Success":
      messages.add_message(self.request, messages.ERROR, response)
      return HttpResponseRedirect(reverse('travel_form'))
    else:
      #Success
      objects = fc.comp_with_plane(objects) if w_plane == 1 else fc.comp_wout_plane(objects)
      self.object = objects
      messages.add_message(self.request, messages.INFO, 'Success.')
      self.object.save()
      return HttpResponseRedirect(reverse('travels'))

class TravelUpdateView(LoginRequiredMixin, UpdateView):
  model = TravelDetails
  form_class = TravelInsertForm
  template_name = settings.BASE_DIR + '/portal/templates/travel_form.html'

  def get_form_kwargs(self):
    kwargs = super().get_form_kwargs()
    kwargs['user'] = self.request.user
    return kwargs
 
  def form_valid(self, form):
    self.object = form.save(commit = False)
    storage = messages.get_messages(self.request)
    storage.used = True
    self.object.name = self.request.user 

    if 'submit' in self.request.POST and self.request.POST["submit"] == "Submit":
      self.object.status = "SUBMITTED"
    else:
      self.object.status = "DRAFT"

    if self.request.user.groups.filter(name__in=["MANAGER","F_MANAGER"]).exists():
      return HttpResponseRedirect(reverse('home'))

    #Validator
    response, objects, w_plane = fc.validator(self.object)

    if response != "Success":
      messages.add_message(self.request, messages.ERROR, response)
      return HttpResponseRedirect(reverse('travel_update_form'))
    else:
      #Success
      objects = fc.comp_with_plane(objects) if w_plane == 1 else fc.comp_wout_plane(objects)
      self.object = objects
      messages.add_message(self.request, messages.INFO, 'Success.')
      self.object.save()
      return HttpResponseRedirect(reverse('travels'))
  
class TravelView(LoginRequiredMixin, ListView): 
  model = TravelDetails
  template_name = settings.BASE_DIR + '/portal/templates/travels.html'
  context_object_name = 'travels'

  def get_queryset(self):
    queryset = super(TravelView, self).get_queryset()
    return queryset.filter(name=self.request.user)

class TravelApproverView(LoginRequiredMixin, ListView): 
  model = TravelDetails
  template_name = settings.BASE_DIR + '/portal/templates/travel_approval.html'
  context_object_name = 'travel_details'

  def get_queryset(self):
    queryset = super(TravelApproverView, self).get_queryset()

    if self.request.user.groups.filter(name="F_MANAGER").exists():
      return queryset.filter(status="SUBMITTED")
    elif self.request.user.groups.filter(name="MANAGER").exists():
      return queryset.filter(
        approver=self.request.user,status="SUBMITTED")
    else:
      return queryset.none()



