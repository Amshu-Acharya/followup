from django.contrib import admin
from .models import Enquiry, Student, Course, Shift, CourseShift, StudentEnrollment

# Register your models here.


admin.site.register([Enquiry, Student, Course, Shift, CourseShift, StudentEnrollment])
