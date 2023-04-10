from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class TeacherInfo(models.Model):
    class Meta:
        verbose_name_plural = 'Teachers Info'
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    salary = models.PositiveIntegerField(null=False)
    joindate = models.DateField(auto_now_add=True)
    mobile = models.CharField(max_length=40)
    status = models.BooleanField(default=False)
    passport = models.ImageField(
        blank=True, null=True, upload_to="static/images/passports/")

    def __str__(self):
        return self.user.first_name

    @property
    def get_id(self):
        return self.user.id

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
