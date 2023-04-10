from django.shortcuts import render, redirect
from django.db.models import Sum
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import NoticeForm
from django.db.models import F
from django.forms.utils import ErrorList
import logging

# |||||| IMPORTING FUNCTIONS FROM OTHER APPS ||||||||||
from general_app. views import is_admin
# |||||| IMPORTING FUNCTIONS FROM OTHER APPS ||||||||||


# |||||| IMPORTING FORMS FROM OTHER APPS ||||||||||
from teachers_app.forms import TeacherUserInfoForm, TeacherInfoForm
from students_app.forms import StudentUserInfoForm, StudentInfoForm
from school_fees_app.forms import TermlyPaymentForm
from payment_app.forms import DailyPaymentForm
# |||||| IMPORTING FORMS FROM OTHER APPS ||||||||||

# |||||| IMPORTING MODELS FROM OTHER APPS ||||||||||
from teachers_app.models import TeacherInfo, User
from students_app.models import StudentInfo
from notice_app.models import Notice
from payment_app.models import Payment
from school_fees_app.models import SchoolFeesPayment
# |||||| IMPORTING MODELS FROM OTHER APPS ||||||||||


@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_homepage_view(request):
    #Get the number of active and pending teachers and students
    active_teachers = TeacherInfo.objects.filter(status=True)
    pending_teachers = TeacherInfo.objects.filter(status=False)
    active_students = StudentInfo.objects.filter(status=True)
    pending_students = StudentInfo.objects.filter(status=False)

    # Get the sum of salaries of active teachers and the total fees of students
    teachers_salary = active_teachers.aggregate(Sum('salary'))['salary__sum']
    students_fees = active_students.count() * 210

    # Get all the notices
    notices = Notice.objects.all()

    # Creating dictionary with the variables to be passed to the template
    context = {
        'active_teachers': active_teachers.count(),
        'pending_teachers': pending_teachers.count(),
        'active_students': active_students.count(),
        'pending_students': pending_students.count(),
        'teachers_salary': teachers_salary,
        'students_fees': students_fees,
        'notices': notices,
    }

    return render(request, 'admin_homepage.html', context)


@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_notice_view(request):
    # form = NoticeForm()
    if request.method == 'POST':
        form = NoticeForm(request.POST)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.by = request.user.first_name
            notice.save()
            return redirect('notice')
    else:
        form = NoticeForm()
    context = {
        'form': form
    }
    return render(request, 'admin_notice.html', context)


def delete_notice_view(request, pk):
    notice = Notice.objects.get(id=pk).delete()
    return redirect('admin_homepage')

# ||||||||||||||||||||||| ALL ABOUT THE TEACHERS |||||||||||||||||||||||||||||||

@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_teacher_homepage_view(request):
    return render(request, 'teachers/admin_teacher_homepage.html')


@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_view_all_teachers_view(request):
    teachers = TeacherInfo.objects.filter(status=True)
    return render(request, 'teachers/admin_view_all_teachers.html', {'teachers': teachers})


@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_add_teacher_view(request):
    if request.method == 'POST':
        user_form = TeacherUserInfoForm(request.POST)
        teacher_form = TeacherInfoForm(request.POST)
        if user_form.is_valid() and teacher_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            teacher = teacher_form.save(commit=False)
            teacher.user = user
            teacher.status = True
            teacher.save()
            messages.success(request, 'New teacher added successfully.')
            return redirect('admin_teacher_homepage')
        else:
            errors = user_form.errors.get_json_data(escape_html=False)
            errors.update(teacher_form.errors.get_json_data(escape_html=False))

            error_list = ErrorList()
            for field,  field_errors in errors.items():
                for error in field_errors:
                    error_list.append(f"{field}: {error['message']}")

            messages.error(request, error_list)      
    else:
        user_form = TeacherUserInfoForm()
        teacher_form = TeacherInfoForm()

    context = {
        'user_form': user_form,
        'teacher_form': teacher_form,
    }

    return render(request, 'teachers/admin_add_teacher.html', context)


@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_update_individual_teacher_info_view(request, pk):
    teacher = TeacherInfo.objects.get(id=pk)
    user = User.objects.get(id=teacher.user_id)

    form1 = TeacherUserInfoForm(instance=user)
    form2 = TeacherInfoForm(instance=teacher)

    if request.method == 'POST':
        if 'update' in request.POST:
            form1 = TeacherUserInfoForm(request.POST, instance=user)
            form2 = TeacherInfoForm(request.POST, instance=teacher)
            if form1.is_valid() and form2.is_valid():
                user = form1.save()
                user.set_password(user.password)
                user.save()
                f2 = form2.save(commit=False)
                f2.save()
                messages.success(request, 'Updating Teacher was successful')
                return redirect('admin_view_all_teachers')
            else:
                messages.error(request, 'Could not update teacher')
                return redirect('admin_view_all_teachers')
        elif 'delete' in request.POST:
            user.delete()
            teacher.delete()
            return redirect('admin_view_all_teachers')
    context = {
        'form1': form1,
        'form2': form2,
    }
    return render(request, 'teachers/admin_update_individual_teacher_info_view.html', context)


@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_approve_teachers_view(request):
    applied_teachers = TeacherInfo.objects.filter(status=False)

    context = {
        'applied_teachers': applied_teachers,
    }
    return render(request, 'teachers/admin_approve_teachers.html', context)

# ||||||||||||||||||||||| END ALL ABOUT THE TEACHERS |||||||||||||||||||||||||||||||


# ||||||||||||||||||||||| ALL ABOUT THE STUDENTS |||||||||||||||||||||||||||||||


@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_student_homepage_view(request):
    return render(request, 'students/students_general/admin_student_homepage.html')


@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_view_all_students_view(request):
    students = StudentInfo.objects.filter(status=True)
    context = {
        'students': students,
    }
    return render(request, 'students/students_general/admin_view_all_students.html', context)


@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_add_student_view(request):


    if request.method == 'POST':
        user_form = StudentUserInfoForm(request.POST)
        student_form = StudentInfoForm(request.POST)
        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            student = student_form.save(commit=False)
            student.user = user
            student.status = True
            if student.payment_method == 'Pay_Per_Day':
                student.termly_debt = 0
            student.save()
            messages.success(request, 'Adding student was successful.')
            return redirect('admin_student_homepage')
        else:
            errors = user_form.errors.get_json_data(escape_html=False)
            errors.update(student_form.errors.get_json_data(escape_html=False))

            error_list = ErrorList()
            for field, field_errors in errors.items():
                for error in field_errors:
                    error_list.append(f"{field}: {error['message']}")

            messages.error(request, error_list)        
    else:    
        user_form = StudentUserInfoForm()
        student_form = StudentInfoForm()    
    context = {
        'user_form': user_form,
        'student_form': student_form,
    }
    return render(request, 'students/students_general/admin_add_student.html', context)


@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_approve_students_view(request):
    students = StudentInfo.objects.filter(status=False)

    context = {
        'students': students,
    }
    return render(request, 'students/students_general/admin_approve_students.html', context)


@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_approve_or_decline_student_view(request, pk):
    if request.method == 'POST':
        if 'approve' in request.POST:
            student = StudentInfo.objects.get(id=pk)
            student.status = True
            student.save()
            messages.success(request, 'Student is now approved')
        elif 'decline' in request.POST:
            student = StudentInfo.objects.get(id=pk)
            student.delete()
    return redirect('admin_approve_students')


@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_view_individual_student_info_view(request, pk):
    student = StudentInfo.objects.get(id=pk)
    payment_record = student.payment_set.all().order_by('-id')
    daily_canteen_record = payment_record.aggregate(daily_canteen=Sum('pay'))
    daily_bus_record = payment_record.aggregate(daily_bus=Sum('carpay'))
    daily_tuition_record = payment_record.aggregate(
        daily_tuition=Sum('schoolfees'))
    if request.method == 'POST':
        if 'delete_student' in request.POST:
            student.status = False
            student.save()
            messages.success(request, 'Deleting student was successful')
            return redirect('admin_view_all_students')
        else:
            messages.error(request, 'Could not delete student')
            return redirect('admin_view_individual_student_info', pk)
        # elif 'delete_payment' in request.POST:

    context = {
        'student': student,
        'payment_record': payment_record,
        'daily_canteen_record': daily_canteen_record,
        'daily_bus_record': daily_bus_record,
        'daily_tuition_record': daily_tuition_record,
    }
    return render(request, 'students/students_general/admin_view_individual_student_info.html', context)


@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_update_individual_student_info_view(request, pk):
    student = StudentInfo.objects.get(id=pk)
    user = User.objects.get(id=student.user_id)

    form1 = StudentUserInfoForm(instance=user)
    form2 = StudentInfoForm(instance=student)
    if request.method == 'POST':
        form1 = StudentUserInfoForm(request.POST, instance=user)
        form2 = StudentInfoForm(request.POST, instance=student)
        if form1.is_valid() and form2.is_valid():
            user = form1.save()
            user.set_password(user.password)
            user.save()
            f2 = form2.save(commit=False)
            f2.status = True
            if f2.payment_method == 'School_Fees_Aside':
                f2.termly_debt = 210
            f2.save()
            messages.success(request, 'Updating Student was successful')
            return redirect('admin_view_individual_student_info', pk)
        else:
            messages.error(request, 'Could not update student')
            return redirect('admin_view_individual_student_info', pk)

    context = {
        'form1': form1,
        'form2': form2,
    }
    return render(request, 'students/students_general/admin_update_individual_student_info.html', context)


# ||||||||||||||||||||||| ALL STUDENTS PAYMENT |||||||||||||||||||||||||||||||


# ||||||||||||||||||||||| ALL STUDENTS PAYMENT |||||||||||||||||||||||||||||||


@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_students_to_pay_view(request):
    students = StudentInfo.objects.filter(status=True, checkifpaiddaily=False)
    all_students = StudentInfo.objects.filter(
        status=True, checkifpaiddaily=True)
    students_paying_per_day = StudentInfo.objects.filter(status=True, payment_method='Pay_Per_Day')
    if request.method == 'POST':
        all_students.update(checkifpaiddaily=False)
        students_paying_per_day.update(termly_debt=0)

    context = {
        'students': students,
    }
    return render(request, 'students/daily_payments/admin_students_to_pay.html', context)


@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_student_daily_payment_view(request, pk):
    student = StudentInfo.objects.get(id=pk)
    payment_form = DailyPaymentForm(initial={'student': student})
    student_pay = student.payment_set.all()
    if request.method == 'POST':
        payment_form = DailyPaymentForm(request.POST)
        # ======================== RESET PAYMENT ========================#
        # ======================== RESET PAYMENT ========================#
        # ======================== RESET PAYMENT ========================#
        if payment_form.is_valid():
            deb = payment_form.cleaned_data['depth']
            bala = payment_form.cleaned_data['balance']
            student.daily_balance = bala
            student.daily_debt = deb
            student.checkifpaiddaily = True
            student.save()
            payment_form.save()
            return redirect('admin_students_to_pay')
    context = {
        'student': student,
        'payment_form': payment_form,
        'student_pay': student_pay
    }
    return render(request, 'students/daily_payments/admin_student_daily_payment_page.html', context)


@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_view_records_of_payment_view(request):
    page_obj = Payment.objects.all().order_by('-id')
    limit_data = Paginator(page_obj, 50)
    page_number = request.GET.get('page')
    try:
        records = limit_data.get_page(page_number)
    except PageNotAnInteger:
        records = limit_data.page(1)
    except EmptyPage:
        records = limit_data(limit_data.num_pages)
    context = {
        'records': records,
    }

    return render(request, 'students/daily_payments/admin_view_records_of_payment.html', context)


@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_view_history_of_daily_total_payment_view(request):

    daily_fee_money_record_obj = Payment.objects.filter().values('when_made').order_by(
        '-when_made').annotate(sum=Sum('pay'), sum2=Sum('carpay'), sum3=Sum('schoolfees'))
    daily_school_fee_money_record = SchoolFeesPayment.objects.filter().values(
        'when_made').order_by('when_made').annotate(sum4=Sum('schoolfees'))

    limit_data = Paginator(daily_fee_money_record_obj, 7)
    page_number = request.GET.get('page')
    try:
        daily_fee_money_record = limit_data.get_page(page_number)
    except PageNotAnInteger:
        daily_fee_money_record = limit_data.page(1)
    except EmptyPage:
        daily_fee_money_record = limit_data(limit_data.num_pages)

    context = {
        'daily_fee_money_record': daily_fee_money_record,
        'daily_school_fee_money_record': daily_school_fee_money_record,
    }
    return render(request, 'students/daily_payments/admin_view_history_of_daily_total_payment.html', context)


@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_daily_paid_students_view(request):
    students = StudentInfo.objects.filter(checkifpaiddaily=True)

    context = {
        'students': students
    }
    return render(request, 'students/daily_payments/admin_daily_paid_students.html', context)


@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_delete_daily_paid_student_view(request, pk):
    students_paid = StudentInfo.objects.get(id=pk)
    last_payment = Payment.objects.filter(student=students_paid)
    delete_last = last_payment.last()
    if request.method == 'POST':
        delete_last.delete()
        students_paid.checkifpaiddaily = False
        students_paid.save()

    return redirect('admin_daily_paid_students')


@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_delete_payment_from_student_profile_view(request, pk):
    if request.method == 'POST':
        if 'delete_payment' in request.POST:
            payment = Payment.objects.get(id=pk)
            payment.delete()
            payment.student.checkifpaiddaily = False
            payment.student.save()
            messages.success(request, 'Deleting payment was successful')
            return redirect('admin_view_individual_student_info', str(payment.student_id))
        else:
            messages.error(request, 'Could not delete this payment')
            return redirect('admin_view_individual_student_info', str(payment.student_id))
    return redirect('admin_view_all_students')


@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_students_to_pay_termly_view(request):
    students = StudentInfo.objects.filter(
        status=True, checkifpaidterm=False)
    student = StudentInfo.objects.all()
    all_students = StudentInfo.objects.filter(
        status=True, checkifpaidterm=True)
    if request.method == 'POST':
        all_students.update(checkifpaidterm=False)

        next_class = {
            'F & B': 'P.S.',
            'P.S.': 'K.S.A.',
            'K.S.A.': 'K.S.B.',
            'K.S.B.': 'K.S.C.',
            'K.S.C.': 'L.S.A.',
            'L.S.A.': 'L.S.B.',
            'L.S.B.': 'L.S.C.'
        }

        students_to_update = []
        for cls in student:
            if cls.cl in next_class:
                cls.cl = next_class[cls.cl]
                students_to_update.append(cls)

        if students_to_update:
            StudentInfo.objects.bulk_update(students_to_update, ['cl']) 

        StudentInfo.objects.filter(payment_method='School_Fees_Aside').update(termly_debt=F('termly_debt')+210, troll=False, soap=False, broom=False)
        StudentInfo.objects.filter(payment_method='Pay_Per_Day').update(termly_debt=0, troll=False, soap=False, broom=False)

    context = {
        'students': students
    }

    return render(request, 'students/termly_payments/admin_students_to_pay_termly.html', context)


@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_student_termly_payment_view(request, pk):
    student = StudentInfo.objects.get(id=pk)
    form = TermlyPaymentForm(initial={'student': student})
    student_pay = student.schoolfeespayment_set.all()
    addedup = student_pay.aggregate(thesum=Sum('schoolfees'))
    if request.method == 'POST':
        form = TermlyPaymentForm(request.POST)
        if form.is_valid():
            deb = form.cleaned_data['debth']
            student.termly_debt = deb
            student.troll = form.cleaned_data['troll']
            student.soap = form.cleaned_data['soap']
            student.broom = form.cleaned_data['broom']
            if form.cleaned_data['debth'] == 0 or form.cleaned_data['debth'] == None and form.cleaned_data['troll'] == True and form.cleaned_data['soap'] == True and form.cleaned_data['broom'] == True:
                student.checkifpaidterm = True
            student.save()
            form.save()
        return redirect('admin_students_to_pay_termly')
    context = {
        'student': student,
        'form': form,
        'student_pay': student_pay,
        'addedup': addedup,
    }
    return render(request, 'students/termly_payments/admin_student_termly_payment_page.html', context)


@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_termly_paid_students_view(request):
    students = StudentInfo.objects.filter(checkifpaidterm=True)
    context = {'students': students}

    return render(request, 'students/termly_payments/admin_termly_paid_students.html', context)


@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_delete_termly_paid_student_view(request, pk):
    students_paid = StudentInfo.objects.get(id=pk)
    last_payment = SchoolFeesPayment.objects.filter(student=students_paid)
    delete_last = last_payment.last()
    print(delete_last)
    if request.method == 'POST':
        delete_last.delete()
        students_paid.checkifpaidterm = False
        students_paid.save()

    return redirect('admin_termly_paid_students')


@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_records_of_all_schoolfees_payment_view(request):
    page_obj = SchoolFeesPayment.objects.all().order_by('-id')
    limit_data = Paginator(page_obj, 50)
    page_number = request.GET.get('page')
    try:
        records = limit_data.get_page(page_number)
    except PageNotAnInteger:
        records = limit_data.get_page(1)
    except EmptyPage:
        records = limit_data(limit_data.num_pages)
    context = {'records': records}
    return render(request, 'students/termly_payments/admin_records_of_all_schoolfees_payment.html', context)


@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_students_with_debt_view(request):
    students = StudentInfo.objects.all()
    context = {
        'students': students
    }
    return render(request, 'students/students_general/admin_students_with_debt.html', context)


# ||||||||||||||||||||||| END OF ALL STUDENTS PAYMENT |||||||||||||||||||||||||||||||



# ||||||||||||||||||||||| END OF ALL ABOUT THE STUDENTS |||||||||||||||||||||||||||||
