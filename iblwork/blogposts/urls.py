from django .urls import path
from blogposts import views
 
urlpatterns = [
    path('', views.index),
     path('posted/subscriber', views.Subscribe, name='subscribe'),
     path('posted/base', views.Subscribe, name='base'),
     path('posted/index', views.index, name= 'about'),
     path('posted/index', views.index, name= 'contact'),
     path('posted/index', views.index, name= 'home'),
     
      
     
 ]
  