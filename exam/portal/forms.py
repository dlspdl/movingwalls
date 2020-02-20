from django import forms
from django.contrib.auth.models import User

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from portal.models import TravelDetails

class TravelInsertForm(forms.ModelForm):
  class Meta:
    model = TravelDetails
    exclude = [
      'name','status','approver_feedback',
      'car_formula','plane_formula'
    ]

  def __init__(self, *args, **kwargs ):
    user = kwargs.pop('user', None)
    super().__init__(*args, **kwargs)
    self.fields["approver"].queryset = User.objects.exclude(username=user)
    self.helper = FormHelper()
    self.helper.form_method = 'post'
    self.helper.add_input(Submit('submit', 'Draft'))
    self.helper.add_input(Submit('submit', 'Submit'))

