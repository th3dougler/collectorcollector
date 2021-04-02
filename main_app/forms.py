from django.forms import ModelForm
from .models import WhatGoesIn

class WhatGoesInForm(ModelForm):
  class Meta:
    model = WhatGoesIn
    fields = ['name', 'colour']