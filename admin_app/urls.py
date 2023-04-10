from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [
    path('homepage/', admin_homepage_view, name='admin_homepage'),

    # ||||||||||||||||||||||| ALL ABOUT THE TEACHERS |||||||||||||||||||||||||||||||
    # ||||||||||||||||||||||| ALL ABOUT THE TEACHERS |||||||||||||||||||||||||||||||
    # ||||||||||||||||||||||| ALL ABOUT THE TEACHERS |||||||||||||||||||||||||||||||
    path('teacher-view/', admin_teacher_homepage_view,
         name='admin_teacher_homepage'),
    path('view-all-teachers/', admin_view_all_teachers_view,
         name='admin_view_all_teachers'),
    path('view-teacher-<str:pk>-info/', admin_update_individual_teacher_info_view,
         name='admin_update_individual_teacher_info'),
    path('add-teacher/', admin_add_teacher_view, name='admin_add_teacher'),
    path('approve-teachers/', admin_approve_teachers_view,
         name='admin_approve_teachers'),

    # ||||||||||||||||||||||| END ALL ABOUT THE TEACHERS |||||||||||||||||||||||||||||||
    # ||||||||||||||||||||||| END ALL ABOUT THE TEACHERS |||||||||||||||||||||||||||||||
    # ||||||||||||||||||||||| END ALL ABOUT THE TEACHERS |||||||||||||||||||||||||||||||
    # ||||||||||||||||||||||| ALL ABOUT THE STUDENTS |||||||||||||||||||||||||||||||
    # ||||||||||||||||||||||| ALL ABOUT THE STUDENTS |||||||||||||||||||||||||||||||
    # ||||||||||||||||||||||| ALL ABOUT THE STUDENTS |||||||||||||||||||||||||||||||
    path('student-view/', admin_student_homepage_view,
         name='admin_student_homepage'),
    path('view-all-students/', admin_view_all_students_view,
         name='admin_view_all_students'),
    path('add-student/', admin_add_student_view, name='admin_add_student'),
    path('not-approved-students/', admin_approve_students_view,
         name='admin_approve_students'),
    path('approve-student/<str:pk>', admin_approve_or_decline_student_view,
         name='admin_approve_or_decline_student'),
    path('view-student-<str:pk>-info', admin_view_individual_student_info_view,
         name='admin_view_individual_student_info'),
    path('update-student-<str:pk>-info/', admin_update_individual_student_info_view,
         name='admin_update_individual_student_info'),
    path('students-to-pay/', admin_students_to_pay_view,
         name='admin_students_to_pay'),
    path('student-id-<str:pk>-paying-today/', admin_student_daily_payment_view,
         name="admin_student_daily_payment"),
    path('records-of-students-payment', admin_view_records_of_payment_view,
         name='records_of_students_payment'),
    path('history-of-total-payment', admin_view_history_of_daily_total_payment_view,
         name='admin_view_history_of_daily_total_payment'),
    path('students-paid-recently', admin_daily_paid_students_view,
         name='admin_daily_paid_students'),
    path('delete-student-<str:pk>-recently-payment', admin_delete_daily_paid_student_view,
         name='admin_delete_daily_paid_student'),
    path('delete-payment/<str:pk>', admin_delete_payment_from_student_profile_view,
         name='admin_delete_payment_from_student_profile'),
    path('students-to-pay-termly', admin_students_to_pay_termly_view,
         name='admin_students_to_pay_termly'),
    path('student-id-<str:pk>-paying-termly/',
         admin_student_termly_payment_view, name='admin_student_termly_payment'),
    path('students-paid-this-term/', admin_termly_paid_students_view,
         name='admin_termly_paid_students'),
    path('delete-student-<str:pk>-termly-payment',
         admin_delete_termly_paid_student_view, name='admin_delete_termly_paid_student'),
    path('records-of-students-schoolfees-payment', admin_records_of_all_schoolfees_payment_view,
         name='admin_records_of_all_schoolfees_payment'),
    path('students-with-debt', admin_students_with_debt_view,
         name='admin_students_with_debt'),



    # ||||||||||||||||||||||| END OF ALL ABOUT THE STUDENTS |||||||||||||||||||||||||||||||
    # ||||||||||||||||||||||| END OF ALL ABOUT THE STUDENTS |||||||||||||||||||||||||||||||
    # ||||||||||||||||||||||| END OF ALL ABOUT THE STUDENTS |||||||||||||||||||||||||||||||
    #
    #
    # |||||||||| URLS INVOLVING OTHER APPS |||||||||||||||||||
    path('notice/', admin_notice_view, name='notice'),
    path('delete-notice/<str:pk>', delete_notice_view, name='delete_notice'),
]
