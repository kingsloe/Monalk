from django.db import models
from students_app.models import StudentInfo


class SchoolFeesPayment(models.Model):
    student = models.ForeignKey(
        StudentInfo, null=True, on_delete=models.SET_NULL)
    schoolfees = models.FloatField(null=True)
    when_made = models.DateField(blank=True, null=True)
    debth = models.FloatField(null=True)
    troll = models.BooleanField(default=False)
    soap = models.BooleanField(default=False)
    broom = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.student
