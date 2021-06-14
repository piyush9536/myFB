from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User

class SignUpForm(UserCreationForm):

    email = forms.EmailField()
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)

    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password1','password2')