from django.db import models
from django.db import models
from django_countries.fields import CountryField

JOB = (
    ('1', "Full time"),
    ('2', "Part time"),
)

WHERE_ARE_FROM = (
    ('1', "international"),
    ('2', "local")
)
FAMILY_STATUS = (
    ('1', "married"),
    ('2', "single"),
    ('3', "divorced"),
)


class InstructorGeneralInfo(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    sex = models.BooleanField(False)
    dob = models.DateField(max_length=8)
    family_status = models.CharField(choices=FAMILY_STATUS, max_length=50)
    children = models.IntegerField()
    department = models.CharField(max_length=100)
    job_time = models.CharField(choices=JOB, max_length=200)
    where_are_from = models.CharField(choices=WHERE_ARE_FROM, max_length=100)
    degree = models.CharField(max_length=200)
    # photo = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.first_name


class InstructorContactInfo(models.Model):
    instructor = models.OneToOneField(InstructorGeneralInfo, on_delete=models.CASCADE, default='')
    phone_number = models.IntegerField()
    country = CountryField()
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    zip_code = models.IntegerField()


class InstructorEducationInfo(models.Model):
    instructor = models.OneToOneField(InstructorGeneralInfo, on_delete=models.CASCADE, default='')
    uni_code = models.IntegerField()
    major_kyr = models.CharField(max_length=100)
    major_rus = models.CharField(max_length=100)
    major_eng = models.CharField(max_length=100)
    degree = models.CharField(max_length=200)
