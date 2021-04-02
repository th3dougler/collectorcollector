from django.urls import path
from . import views

urlpatterns = [
    path('', views.CollectorHome.as_view() , name="collector-home"),
    path('about/', views.CollectorAbout.as_view(), name="collector-about"),
    path('index/', views.CollectorList.as_view(), name="collector-list"),
    path('create/', views.CollectorCreate.as_view(), name="collector-create"),
    path('<int:pk>/', views.CollectorDetail.as_view(), name="collector-detail"),
    path('<int:pk>/update/', views.CollectorUpdate.as_view(), name="collector-update"),
    path('<int:pk>/delete/', views.CollectorDelete.as_view(), name="collector-delete"),  
    path('<int:pk>/add_whatgoesin/', views.add_whatgoesin, name="add_whatgoesin"),  
    
]