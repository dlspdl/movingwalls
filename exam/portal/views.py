import os

from django.conf import settings
from django.views.generic import CreateView
from portal.forms import TravelForm
from portal.models import TravelDetails

class TraverlInsertView(CreateView):
    model = TravelDetails
    form_class = TravelForm
    template_name = os.path.join(settings.BASE_DIR, 'portal/templates/travel_form.html')
