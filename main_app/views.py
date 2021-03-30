from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from .models import Collector

class CollectorHome(TemplateView):
    template_name = "main_app/collector_home.html"

class CollectorAbout(TemplateView):
    template_name = "main_app/collector_about.html"
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = 'about' 
        return context
    
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
    
class CollectorCreate(CreateView):
    model = Collector
    fields = '__all__'


class CollectorUpdate(UpdateView):
    model = Collector
    fields = '__all__'

class CollectorDelete(DeleteView):
    model = Collector
    success_url = reverse_lazy('collector-list')

