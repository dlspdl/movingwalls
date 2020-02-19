from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from portal import functions as fc
from portal.models import Airport, Hotel, Fare 
from portal.models import FareFormula, Location, TravelDetails

class TravelMgrApprovalAPI(LoginRequiredMixin,APIView):
  parser_classes = [JSONParser] 
  
  def post(self, request, format=None):
    pk = request.data["pk"]
    reason = request.data["reason"]
    status = request.data["status"]
    
    try: 
      details = TravelDetails.objects.get(pk=pk)
      details.status = status
      details.approver_reason = reason 
      details.save()
      return Response(status=201)
    except TravelDetails.DoesNotExist:
      return Response(status=400)

#class TravelFMgrApprovalAPI(LoginRequiredMixin, APIView):
#  def post(self, request, format=None):
#    pk = request.pk
#    reason = request.reason
#    status = request.status
#    user = request.user
#    
#    try: 
#      details = TravelDetails.objects.get(pk=pk,approver=user)
#      details.status = status
#      details.approver_reason = reason 
#      return response(status=201)
#    except TravelDetails.DoesNotExist:
#      return response(status=400)
