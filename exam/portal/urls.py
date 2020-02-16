from django.urls import path

from portal.views import TravelInsertView, TravelView 

urlpatterns = [
  path('travel/', TravelView.as_view(), name='travels' ),
  path('travel/form/', TravelInsertView.as_view(), name='travelform' ),
]
