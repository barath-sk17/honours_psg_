from rest_framework import serializers
from .models import Semester, Year, Course, Faculty, Student,\
    Attendance, CourseIndex, FacultyIndex, StudentIndex

class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = '__all__'

class YearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Year
        fields = '__all__'
        
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        
class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'
        
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'
        
class CourseIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseIndex
        fields = '__all__'
        
class FacultyIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacultyIndex
        fields = '__all__'
        
class StudentIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentIndex
        fields = '__all__'