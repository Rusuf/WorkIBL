from django import forms

from .models import Subscriber



class SubscriberForm(forms.Form):
      
        email = forms.EmailField(label='Email', max_length=100)
        class meta:
                model = Subscriber
        
       