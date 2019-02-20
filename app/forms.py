from django import from
from models import *

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)


    class Meta:
        models = User
        fields = ('username','name','email','password')