import email
from django.forms import ModelForm
from .models import Subscriber
from blogposts.models import models
from django import forms



class SubscriberForm(ModelForm):
    email = forms.TextInput()
    class Meta:
        model = Subscriber
        fields = ('email',)
    

      
       