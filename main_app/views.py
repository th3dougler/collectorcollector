from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required


from .models import Collector, Common_Feature
from .forms import WhatGoesInForm, CommonFeatureForm

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
        context['object_list'] = Collector.objects.filter(user=self.request.user)
        return context
    
class CollectorDetail(DetailView):
    model = Collector
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = 'detail'
        print(context)
        context['whatgoesin_form'] = WhatGoesInForm()
        context['common_feature_form'] = CommonFeatureForm()
        context['common_feature_list'] = Common_Feature.objects.exclude(id__in = context['collector'].common_feature.all().values_list('id'))
        return context
    
class CollectorCreate(CreateView):
    model = Collector
    fields = ['name','category','description','capacity','common_feature']
    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the cat
        # Let the CreateView do its job as usual
        return super().form_valid(form)


class CollectorUpdate(UpdateView):
    model = Collector
    fields = '__all__'

class CollectorDelete(DeleteView):
    model = Collector
    success_url = reverse_lazy('collector-list')

@login_required
def add_whatgoesin(request, pk):
    form = WhatGoesInForm(request.POST)
    if form.is_valid():
        new_thingthatgoesin = form.save(commit=False)
        new_thingthatgoesin.collector_id = pk
        new_thingthatgoesin.save()
    return redirect('collector-detail', pk=pk)

@login_required
def assoc_feature(request, pk, feat_id):
    Collector.objects.get(id=pk).common_feature.add(feat_id)
    return redirect('collector-detail', pk=pk)
    
    
class FeatureCreate(CreateView):
    model = Common_Feature
    fields = '__all__'
    
class FeatureDetail(DetailView):
    model = Common_Feature
    
    
class FeatureList(ListView):
    model = Common_Feature
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = 'list-feature'
        return context
    
class FeatureUpdate(UpdateView):
    model = Common_Feature
    fields = '__all__'

class FeatureDelete(DeleteView):
    model = Common_Feature
    template_name = 'main_app/collector_confirm_delete.html'
    success_url = reverse_lazy('common-feature-list')
    
def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('collector-list')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)