from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from portal.models import TravelDetails

class TravelForm(forms.ModelForm):
  class Meta:
    model = TravelDetails
    fields = (
      'origin', 'mode_of_travel', 'start_date', 'end_date', 
      'airport_origin', 'airport_dest', 'hotel', 'approver'
    )

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.form_method = 'post'
    self.helper.add_input(Submit('submit', 'Draft'))
    self.helper.add_input(Submit('submit', 'Submit'))
