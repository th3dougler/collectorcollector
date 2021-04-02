from django.contrib import admin

from .models import Collector, WhatGoesIn, Common_Feature
# Register your models here.

admin.site.register(Collector)
admin.site.register(WhatGoesIn)
admin.site.register(Common_Feature)

