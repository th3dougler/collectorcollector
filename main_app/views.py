from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from .models import Collector

class CollectorList(ListView):
    model = Collector
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = 'index'
        return context
    
class CollectorDetail(DetailView):
    model = Collector
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = 'detail'
        return context

class CollectorHome(TemplateView):
    template_name = "main_app/collector_home.html"

class CollectorAbout(TemplateView):
    template_name = "main_app/collector_about.html"
    