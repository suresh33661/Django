from django.urls import path
from first_app import views
from .views import Home

urlpatterns = [
    
    path('',Home.as_view(),name='home'),
   
]
