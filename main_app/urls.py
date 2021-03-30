from django.urls import path
from . import views

urlpatterns = [
    path('', views.CollectorHome.as_view() , name="collector-home"),
    path('about/', views.CollectorAbout.as_view(), name="collector-about"),
    path('index/', views.CollectorList.as_view(), name="collector-list"),
    path('<int:pk>/', views.CollectorDetail.as_view(), name="collector-detail"),
    path('create/', views.CollectorCreate.as_view(), name="collector-create"),
    
]