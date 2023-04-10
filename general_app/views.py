from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login
from students_app.models import *
# Create your views here.


def is_admin(user):
    return user.groups.filter(name='ADMIN').exists


def is_student(user):
    return user.groups.filter(name='STUDENT').exists


def is_teacher(user):
    return user.groups.filter(name='TEACHER').exists


def is_admin_in(user):
    return user.groups.filter(name='ADMIN')


def is_student_in(user):
    return user.groups.filter(name='STUDENT')


def is_teacher_in(user):
    return user.groups.filter(name='TEACHER')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if is_student_in(request.user):
                accountapproval = StudentInfo.objects.filter(
                    user_id=request.user.id, status=True)
                if accountapproval:
                    return redirect('homepage')
                else:
                    return render(request, 'student_wait_for_approval.html',)

            return redirect('homepage')
    context = {}
    return render(request, 'login.html', context)


def singup_options_view(request):
    return render(request, 'signup_options.html')


def homepage_view(request):
    return render(request, 'general_homepage.html')


def aboutus_view(request):
    return render(request, 'aboutus.html')


def send_email_view(request):
    if request.method == 'POST':
        template = render_to_string('email_template.txt', {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'message': request.POST['message'],
        })
        email = EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER,
            ['nanayawdjan446@gmail.com']
        )
        email.fail_silently = False
        email.send()
        messages.success(request, 'Reaching out to us was successfull.')
    return render(request, 'aboutus.html')
