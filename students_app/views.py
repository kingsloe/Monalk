from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.models import Group
from django.contrib import messages
from notice_app.models import Notice

# Create your views here.


def student_signup_view(request):
    form1 = StudentUserInfoForm()
    form2 = OutsideStudentInfoForm()

    if request.method == 'POST':
        form1 = StudentUserInfoForm(request.POST)
        form2 = OutsideStudentInfoForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            print('worked')
            user = form1.save()
            user.set_password(user.password)
            user.save()
            f2 = form2.save(commit=False)
            f2.user = user
            f2.save()

            my_student_group = Group.objects.get_or_create(name='STUDENT')
            my_student_group[0].user_set.add(user)
            messages.success(request, 'Signing up was successful')
            return redirect('login')
        else:
            messages.error(request, 'Could not sign up')

    context = {
        'form1': form1,
        'form2': form2,
    }
    return render(request, 'student_signup.html', context)


def student_homepage_view(request):
    studentdata = StudentInfo.objects.all().filter(
        status=True, user_id=request.user.id)
    notice = Notice.objects.all()
    method = studentdata[0].payment_method == 'School_Fees_Aside'
    print(method)

    context = {
        'name': studentdata[0].get_name,
        'roll': studentdata[0].roll,
        'gender': studentdata[0].gender,
        'mother': studentdata[0].mother,
        'father': studentdata[0].father,
        'residence': studentdata[0].residence,
        'date_of_birth': studentdata[0].date_of_birth,
        'date_of_admission': studentdata[0].date_of_admission,
        'cl': studentdata[0].cl,
        'notice': notice,
        'debt': studentdata[0].daily_debt,
        'balance': studentdata[0].daily_balance,
        'termly_debt': studentdata[0].termly_debt,
        'method': method,
    }
    return render(request, 'student_homepage.html', context)
