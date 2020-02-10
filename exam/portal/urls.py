from django.urls import path

from portal.views import TraverlInsertView 

urlpatterns = [
  path('travelform/', TraverlInsertView.as_view(), name='travelform' ),
]
