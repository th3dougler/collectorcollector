from django.urls import path
from . import views
from .views import CollectorList, CollectorDetail, CollectorHome, CollectorAbout

urlpatterns = [
    path('', CollectorHome.as_view() , name="collector-home"),
    path('index/', CollectorList.as_view(), name="collector-list"),
    path('about/', CollectorAbout.as_view(), name="collector-about"),
    path('<int:pk>/', CollectorDetail.as_view(), name="collector-detail")

]