from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class UserCreationForm(UserCreationForm):
    """docstring for ."""
    class Meta:
        model = User
        fields = ['username','email']

#para criar pelo django admin
class UserAdminForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','name','is_active','is_staff']
        
