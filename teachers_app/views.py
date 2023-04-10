from django.shortcuts import render

# Create your views here.


def teacher_signup_view(request):
    context = {}
    return render(request, 'teacher_signup.html', context)
