from django import forms
from .models import *
import datetime


class TermlyPaymentForm(forms.ModelForm):
    when_made = forms.DateField(initial=datetime.date.today)

    class Meta:
        model = SchoolFeesPayment
        fields = ['student', 'schoolfees', 'when_made',
                  'debth', 'troll', 'soap', 'broom']
