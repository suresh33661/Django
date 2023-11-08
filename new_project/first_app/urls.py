from django.urls import path
from first_app import views

urlpatterns = [
    
    path('',views.homepage,name='homepage'),
    path('about/',views.about,name='about')
]
