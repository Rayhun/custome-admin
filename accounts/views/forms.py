from django.forms import ModelForm
from django import forms
from django.contrib.auth import get_user_model 
from accounts.models import Profile

User = get_user_model()

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name',)

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']