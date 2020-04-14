from django.contrib import admin
from .models import InstructorContactInfo,InstructorEducationInfo, InstructorGeneralInfo

admin.site.register(InstructorContactInfo)
admin.site.register(InstructorGeneralInfo)
admin.site.register(InstructorEducationInfo)


# Register your models here.
