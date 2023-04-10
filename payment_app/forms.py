from django import forms
from .models import *
import datetime


class DailyPaymentForm(forms.ModelForm):
    when_made = forms.DateField(initial=datetime.date.today)

    class Meta:
        model = Payment
        fields = ['student', 'pay', 'carpay', 'schoolfees',
                  'balance', 'depth', 'when_made']
