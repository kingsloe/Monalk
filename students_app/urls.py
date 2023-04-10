from django.urls import path
from .views import *


urlpatterns = [
    path('signup/', student_signup_view, name='student_signup'),
]
