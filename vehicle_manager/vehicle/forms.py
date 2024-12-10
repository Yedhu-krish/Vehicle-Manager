from django import  forms

from vehicle.models import Vehicle

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

class VehicleCreateForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control mb-3'}))
    type = forms.ChoiceField(choices=Vehicle.TYPE_OPTIONS,widget=forms.Select(attrs={'class':'form-control form-select mb-3'}))
    engine = forms.ChoiceField(choices=Vehicle.ENGINE_TYPES,widget=forms.Select(attrs={'class':'form-control form-select mb-3'}))
    fuel = forms.ChoiceField(choices=Vehicle.FUEL_OPTIONS,widget=forms.Select(attrs={'class':'form-control form-select mb-3'}))
    amount = forms.FloatField(widget=forms.NumberInput(attrs={'class':'form-control mb-3'}))


class SignUpForm(UserCreationForm):

    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control placeholder:Enter password'}))

    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control placeholder:Confirm password'}))


    class Meta:

        model = User

        fields = ['username','email','password1','password2']

        widgets = {

            'username':forms.TextInput(attrs={'class':'form-control'}),

            'email':forms.EmailInput(attrs={'class':'form-control'})
        }

class LoginForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your username'}))

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your password'}))
        
    



