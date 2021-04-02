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
    path('<int:pk>/assoc_feature/<int:feat_id>', views.assoc_feature, name="assoc_feature"), 
    
    
    path('feature/index/', views.FeatureList.as_view(), name="common-feature-list"),
    path('feature/create/', views.FeatureCreate.as_view(), name="common-feature-create"),
    path('feature/<int:pk>/', views.FeatureDetail.as_view(), name="common-feature-detail"),
    path('feature/<int:pk>/update/', views.FeatureUpdate.as_view(), name="common-feature-update"),
    path('feature/<int:pk>/delete/', views.FeatureDelete.as_view(), name="common-feature-delete"),  
    # path('<int:pk>/assoc_feature/<int:feat_key>', views.add_whatgoesin, name="assoc_feature"), 
]