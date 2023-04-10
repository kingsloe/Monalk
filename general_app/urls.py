from django.urls import path
from .views import *
from admin_app.views import admin_homepage_view
from students_app.views import student_homepage_view
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', homepage_view, name='homepage'),
    path('aboutus/', aboutus_view, name='aboutus'),
    path('send-email/', send_email_view, name="send_email"),
    path('login/', login_view, name='login'),
    path('logout', LogoutView.as_view(
        template_name='general_homepage.html'), name='logout'),
    path('admin/admin-homepage/', admin_homepage_view, name='admin-homepage'),
    path('student/student-homepage/', student_homepage_view,
         name='student-homepage'),
    path('signup-options/', singup_options_view, name='signup_options'),
]
