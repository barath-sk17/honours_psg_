from django.db import models

# Semester ---> Even / Odd
class Semester(models.Model):
    TYPE_CHOICES = [
        ('Odd', 'Odd'),
        ('Even', 'Even'),
    ]
    sem = models.CharField(max_length=15, choices=TYPE_CHOICES,unique=True)
    
    def _str_(self):
        return self.sem
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['sem'], name="unique_combination1")
        ]
    
# Year ---> ex : 2023 (every year records)
class Year(models.Model):
    year = models.CharField(max_length=7)
    sem = models.ForeignKey(
        Semester, on_delete=models.CASCADE,
        related_name='years',
    )

    class Meta:
        unique_together = [('year', 'sem')]


class CourseIndex(models.Model):
    course_id = models.CharField(max_length=10,unique=True)
    course_name = models.CharField(max_length=50,unique=True)
    
class FacultyIndex(models.Model):
    faculty_id = models.CharField(max_length=10,unique=True)
    faculty_name = models.CharField(max_length=50)
    
    class Meta:
        unique_together = [('faculty_id', 'faculty_name')]

class StudentIndex(models.Model):
    student_id = models.CharField(max_length=10,unique=True)
    student_name = models.CharField(max_length=50)
    
    class Meta:
        unique_together = [('student_id', 'student_name')]

# Course ---> ex : course name and course_id (along with year)
class Course(models.Model):
    course = models.ForeignKey(
        CourseIndex, on_delete=models.CASCADE,
        related_name='courseindex'
    )
    course_year = models.ForeignKey(
        Year, on_delete=models.CASCADE,
        related_name='courses'
    )
    class Meta:
        unique_together = [('course', 'course_year')]


        
class Faculty(models.Model):
    faculty = models.ForeignKey(
        FacultyIndex, on_delete=models.CASCADE,
        related_name='facultyindex'
    )
    course_id = models.ForeignKey(
        Course, on_delete=models.CASCADE,
        related_name='faculties',
    )
    faculty_year = models.ForeignKey(
        Year, on_delete=models.CASCADE,
        related_name='facultyyear'
    )
    
    class Meta:
        unique_together = [('faculty', 'course_id','faculty_year')]

class Student(models.Model):
    student = models.ForeignKey(
        StudentIndex, on_delete=models.CASCADE,
        related_name='studentindex'
    )
    course_id = models.ForeignKey(
        Faculty, on_delete=models.CASCADE,
        related_name='students',
    )
    student_year = models.ForeignKey(
        Year, on_delete=models.CASCADE,
        related_name='studentyear'
    )
    
    class Meta:
        unique_together = [('student', 'course_id','student_year')]

#
class Attendance(models.Model):
    attend = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
    ]
    student_detail = models.ForeignKey(
        Student, on_delete=models.CASCADE,
        related_name='atendance_student'
    )
    date = models.DateField()
    hrs = models.IntegerField()
    status = models.CharField(max_length=15, choices=attend)
    class Meta:
        unique_together = [('student_detail', 'hrs', 'status', 'date')]
        