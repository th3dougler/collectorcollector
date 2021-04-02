from django.forms import ModelForm
from .models import WhatGoesIn, Common_Feature

class WhatGoesInForm(ModelForm):
  class Meta:
    model = WhatGoesIn
    fields = ['name', 'colour']
    
class CommonFeatureForm(ModelForm):
    class Meta:
        model = Common_Feature
        fields = ['name']