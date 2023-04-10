from django import forms
from django.contrib.auth.models import User
from .models import StudentInfo


class StudentUserInfoForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                  'username', 'password']


class StudentInfoForm(forms.ModelForm):
    class Meta:
        model = StudentInfo
        fields = ['roll', 'cl', 'mobile', 'fee', 'status',
                  'date_of_admission', 'date_of_birth', 'gender', 'mother', 'father',
                  'residence', 'foodfee', 'carfee', 'payment_category', 'payment_method',
                  'form_of_transportation', 'passport']


class OutsideStudentInfoForm(forms.ModelForm):
    class Meta:
        model = StudentInfo
        fields = ['date_of_admission', 'date_of_birth',
                  'gender', 'mother', 'father', 'mobile',
                  'passport', 'cl', 'residence', 'payment_category',
                  'payment_method', 'form_of_transportation']
