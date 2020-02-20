from django.urls import path

from portal.views.pages import TravelView 
from portal.views.pages import TravelApproverView 
from portal.views.pages import TravelInsertView
from portal.views.api import TravelFMgrApprovalAPI
from portal.views.api import TravelMgrApprovalAPI

urlpatterns = [
  path('travel/', TravelView.as_view(), name='travels' ),
  path('travel/approver/', TravelApproverView.as_view(), name='travel_approver' ),
  path('travel/form/', TravelInsertView.as_view(), name='travel_form' ),
  path('travel/fmgr/change_status/', TravelFMgrApprovalAPI.as_view(), name='travel_fmgr_approval' ),
  path('travel/mgr/change_status/', TravelMgrApprovalAPI.as_view(), name='travel_mgr_approval' ),
]
