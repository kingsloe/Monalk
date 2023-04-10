from django.db import models
from students_app.models import StudentInfo

# Create your models here.


class Payment(models.Model):
    student = models.ForeignKey(
        StudentInfo, null=True, on_delete=models.SET_NULL, blank=True)
    pay = models.FloatField(null=True, blank=True, default=0)
    carpay = models.FloatField(null=True, blank=True, default=0)
    schoolfees = models.FloatField(null=True, blank=True, default=0)
    when_made = models.DateField(blank=True, null=True)
    balance = models.FloatField(null=True)
    depth = models.FloatField(null=True)

    # def __str__(self):
    #     return self.student
