from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from portal import functions as fc
from portal.models import Airport, Hotel, Fare 
from portal.models import FareFormula, Location, TravelDetails

class TravelDeleteAPI(LoginRequiredMixin,APIView):
  parser_classes = [JSONParser] 
  
  def post(self, request, format=None):
    data = request.data
    data["user"] = request.user
    
    try: 
      details = TravelDetails.objects.get(pk=data["pk"],approver=data["user"])
      details.delete()
      return Response(status=201)
    except TravelDetails.DoesNotExist:
      return Response(status=400)

class TravelMgrApprovalAPI(LoginRequiredMixin,APIView):
  parser_classes = [JSONParser] 
  
  def post(self, request, format=None):
    if not user.groups.filter(name="MANAGER").exists():
      return Response(status=403)

    data = request.data
    data["user"] = request.user
    
    try: 
      details = TravelDetails.objects.get(pk=data["pk"],approver=data["user"])
      details.status = data["status"]
      details.approver_reason = data["approver_reason"] 
      details.save()
      return Response(status=201)
    except TravelDetails.DoesNotExist:
      return Response(status=400)

class TravelFMgrApprovalAPI(LoginRequiredMixin,APIView):
  parser_classes = [JSONParser] 
  
  def post(self, request, format=None):
    if not user.groups.filter(name="F_MANAGER").exists():
      return Response(status=403)

    data = request.data
    
    try: 
      details = TravelDetails.objects.get(pk=data["pk"])
      details.status = data["status"]
      details.approver_reason = data["approver_reason"] 
      details.save()
      return Response(status=201)
    except TravelDetails.DoesNotExist:
      return Response(status=422)
