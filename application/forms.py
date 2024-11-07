from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Customer,Destination

class CustomerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Customer
        fields = UserCreationForm.Meta.fields + ('first_name','last_name','email','full_address',)


class CustomerUpdateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'full_address']
        widgets = {
            'email': forms.EmailInput(attrs={'readonly': True}),  # If you want to make the email read-only
        }

class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ['name', 'description', 'region']

from .models import Itinerary

class ItineraryForm(forms.ModelForm):
    class Meta:
        model = Itinerary
        fields = ['name', 'destination', 'start_date', 'end_date', 'notes']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'datepicker'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'datepicker'}),
            'notes': forms.Textarea(attrs={'class': 'materialize-textarea'}),
        }

    def __init__(self, *args, **kwargs):
        super(ItineraryForm, self).__init__(*args, **kwargs)
        self.fields['destination'].queryset = Destination.objects.all()

from .models import Activity

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['name', 'description', 'estimated_cost']