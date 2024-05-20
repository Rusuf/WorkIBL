from django .urls import path
from . import views
 
urlpatterns = [
     path('', views.index),
     path('posted/subscriber', views.Subscribe),
     
 ]
 