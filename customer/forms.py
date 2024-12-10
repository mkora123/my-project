from django import forms
from django.template.defaultfilters import title

from customer.models import Customer, Doctor, Appointment
from django.forms.widgets import ClearableFileInput

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


        widgets = {

            'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your name'}),

            'email' : forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter your email'}),
            'gender' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your gender'}),
            'age' : forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter your age'}),
            'image' : ClearableFileInput(attrs={
                'class':'form-control',
                'accept' : 'images/*',
                'title':'Upload your image here'}),
        }


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'




class LoginForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your username'}),
            'password' : forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your password'}),
        }











