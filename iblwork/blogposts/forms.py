from django import forms
from django.forms import ModelForm


from .models import Subscriber
from .models import Subscriber

class SubscriberForm(ModelForm):
    email = forms.EmailField()
    created_at = forms.DateTimeField()
    updated_at = forms.DateTimeField()
    class Meta:
        model = Subscriber()
        fields = ['email']