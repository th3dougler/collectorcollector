from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('', views.CollectorHome.as_view() , name="collector-home"),
    path('about/', views.CollectorAbout.as_view(), name="collector-about"),
    path('index/', login_required(views.CollectorList.as_view()), name="collector-list"),
    path('create/', login_required(views.CollectorCreate.as_view()), name="collector-create"),
    path('<int:pk>/', login_required(views.CollectorDetail.as_view()), name="collector-detail"),
    path('<int:pk>/update/', login_required(views.CollectorUpdate.as_view()), name="collector-update"),
    path('<int:pk>/delete/', login_required(views.CollectorDelete.as_view()), name="collector-delete"), 
    
    path('<int:pk>/add_whatgoesin/', views.add_whatgoesin, name="add_whatgoesin"),  
    path('<int:pk>/assoc_feature/<int:feat_id>', views.assoc_feature, name="assoc_feature"), 
    
    
    path('feature/index/', login_required(views.FeatureList.as_view()), name="common-feature-list"),
    path('feature/create/', login_required(views.FeatureCreate.as_view()), name="common-feature-create"),
    path('feature/<int:pk>/', login_required(views.FeatureDetail.as_view()), name="common-feature-detail"),
    path('feature/<int:pk>/update/', login_required(views.FeatureUpdate.as_view()),name="common-feature-update"),
    path('feature/<int:pk>/delete/', login_required(views.FeatureDelete.as_view()), name="common-feature-delete"),  
    
    path('accounts/signup/', views.signup, name="signup"), 
]