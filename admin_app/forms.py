from notice_app.models import Notice
from django import forms


class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = '__all__'
