from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UsernameField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Notes, Contact

class MyloginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": False, 'class':'form-field', 'placeholder':'Username'}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", 'class':'form-field', 'placeholder':'Password'}),
    )

class SignUpForm(UserCreationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'class':'form-field','placeholder':'Username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-field','placeholder':'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-field','placeholder':'Last Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-field','placeholder':'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-field','placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-field','placeholder':'Confirm Password'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        label = {'email':'Email'}

class NotesForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-field', 'placeholder':'Title'}))
    discription = forms.CharField(widget=forms.TextInput(attrs={'class':'form-field', 'placeholder':'Description'}))
    class Meta:
        model = Notes
        fields = ['title', 'discription']

class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
    contactNo = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Contact Number'}))
    message = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Message'}))
    class Meta:
        model = Contact
        fields = ['name', 'email', 'contactNo', 'message']