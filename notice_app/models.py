from django.db import models

# Create your models here.


class Notice(models.Model):
    date = models.DateField(auto_now=True)
    by = models.CharField(max_length=20, null=True, default='school')
    message = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = 'Notice'
