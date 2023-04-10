from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', teacher_signup_view, name='teacher_signup')
]
