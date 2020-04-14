from django.db import models

class Major(models.Model):
    majorrus = models.CharField(max_length=50)
    majoreng = models.CharField(max_length=50)
    majorkyr = models.CharField(max_length=50)
    licence = models.CharField(max_length=20, blank=True)
    year_of_educ = models.IntegerField(default=4)


class StudentGeneralInfo(models.Model):
    sid = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    sex = models.BooleanField(default=False)
    birth_date = models.DateField()
    # ncode = models.IntegerField()
    # ccode = models.IntegerField()
    army_service = models.BooleanField(default=False)
    rtoefl = models.IntegerField()

    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Dismissed', 'Dismissed'),
        ('Academic leave', 'Academic leave'),
        ('Graduate', 'Graduate'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active')
    major = models.ForeignKey(Major, on_delete=models.CASCADE)

    def __str__(self):
        return self.last_name

