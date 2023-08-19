from django.contrib import admin

# Register your models here.
from .models import Semester, Year, Course, Faculty, Student, Attendance, CourseIndex, \
    StudentIndex, FacultyIndex

admin.site.register(Semester)
admin.site.register(Year)
admin.site.register(Course)
admin.site.register(Faculty)
admin.site.register(Student)
admin.site.register(Attendance)
admin.site.register(CourseIndex)
admin.site.register(FacultyIndex)
admin.site.register(StudentIndex)