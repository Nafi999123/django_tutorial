
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('index/', views.index, name='Home'),  
    path('about/', views.about,name='About'),  
    path('booking/', views.booking,name='Booking'),  
    path('doctors/', views.doctors,name='Doctors'),  
    path('contact/', views.contact,name='Contact'),  
    path('department/', views.department,name='Department'),  
]