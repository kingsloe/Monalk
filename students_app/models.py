from django.db import models
from django.contrib.auth.models import User

# Create your models here.
COMING_FROM = [
    ('Dwenem', 'Dwenem'),
    ('Mpuasu', 'Mpuasu'),
    ('Adamsu', 'Adamsu'),
    ('Bodaa', 'Bodaa'),
    ('Kofitia', 'Kofitia'),
    ('Adiokor1', 'Adiokor1'),
    ('Adiokor2', 'Adiokor2'),
    ('Zezera', 'Zezera'),
    ('Kwamepim', 'Kwamepim'),
    ('Kotokware', 'Kotokware'),
]

GENDER = [
    ('Male', 'Male'),
    ('Female', 'Female')
]

CLASSES = [
    ('F & B', 'F & B'),
    ('P.S.', 'P.S.'),
    ('K.S.A.', 'K.S.A.'),
    ('K.S.B.', 'K.S.B.'),
    ('K.S.C.', 'K.S.C.'),
    ('L.S.A.', 'L.S.A.'),
    ('L.S.B.', 'L.S.B.'),
    ('L.S.C.', 'L.S.C.')
]

FORM_OF_TRANSPORTATION = [
    ('Bus', 'Bus'),
    ('Walk', 'Walk')
]

PAYMENT_METHOD = [
    ('Pay_Per_Day', 'Pay Per Day'),
    ('School_Fees_Aside', 'School Fees Aside')

]

PAYMENT_CATEGORY = [
    ('Pay_Everything', 'Pay Everything'),
    ('Dont_Pay', 'Don\'t Pay'),
    ('Considered', 'Considered'),
]


class StudentInfo(models.Model):
    class Meta:
        verbose_name_plural = 'Student Info'

    roll = models.CharField(max_length=10)
    date_of_admission = models.DateField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=45, null=True, choices=GENDER)
    mother = models.CharField(max_length=45, null=True, blank=True)
    father = models.CharField(max_length=45, null=True, blank=True)
    mobile = models.CharField(max_length=40, null=True, blank=True)
    cl = models.CharField(max_length=10, choices=CLASSES, null=True)
    residence = models.CharField(max_length=45, null=True, choices=COMING_FROM)
    fee = models.FloatField(null=True, default=210)
    foodfee = models.FloatField(null=True, blank=True)
    carfee = models.FloatField(null=True, blank=True)
    status = models.BooleanField(default=False)
    checkifpaiddaily = models.BooleanField(default=False)
    checkifpaidterm = models.BooleanField(default=False)
    daily_debt = models.FloatField(null=True, blank=True, default=0)
    daily_balance = models.FloatField(null=True, blank=True, default=0)
    termly_debt = models.FloatField(null=True, blank=True, default=210)
    payment_category = models.CharField(
        max_length=40, choices=PAYMENT_CATEGORY, null=True)
    form_of_transportation = models.CharField(
        max_length=40, choices=FORM_OF_TRANSPORTATION, null=True)
    payment_method = models.CharField(
        max_length=40, choices=PAYMENT_METHOD, null=True)
    troll = models.BooleanField(default=False)
    soap = models.BooleanField(default=False)
    broom = models.BooleanField(default=False)

    passport = models.ImageField(
        blank=True, null=True, upload_to="static/images/passports/")

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name

    @property
    def get_id(self):
        return self.user.id
    
    # @property
    # def get_those_with_termly_debt(self):
    #     return self.

    def __str__(self):
        return self.user.first_name+' '+self.user.last_name
