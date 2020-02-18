from django.urls import path

from portal.views import TravelView 
from portal.views import TravelApproverView 
from portal.views import TravelInsertView

urlpatterns = [
  path('travel/', TravelView.as_view(), name='travels' ),
  path('travel/approver/', TravelApproverView.as_view(), name='travel_approver' ),
  path('travel/form/', TravelInsertView.as_view(), name='travelform' ),
]
