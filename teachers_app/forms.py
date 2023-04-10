from django import forms
from django.contrib.auth.models import User
from .models import TeacherInfo


class TeacherUserInfoForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']


class TeacherInfoForm(forms.ModelForm):
    class Meta:
        model = TeacherInfo
        fields = ['salary', 'mobile', 'status', 'passport', 'status']
