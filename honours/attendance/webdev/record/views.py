from record.models import Semester, Year, Course, Faculty, Student,\
    Attendance, CourseIndex, FacultyIndex, StudentIndex
from django.template.defaulttags import register
from rest_framework import viewsets
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from record.serializers import SemesterSerializer, YearSerializer,\
    CourseSerializer, FacultySerializer, StudentSerializer, AttendanceSerializer, \
    CourseIndexSerializer, StudentIndexSerializer, FacultyIndexSerializer
import json

@register.filter
def getrange(value):
    return range(1,value+1)

class SemesterViewSet(viewsets.ModelViewSet):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer  

class YearViewSet(viewsets.ModelViewSet):
    queryset = Year.objects.all()
    serializer_class = YearSerializer
    
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
class FacultyViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    
class CourseIndexViewSet(viewsets.ModelViewSet):
    queryset = CourseIndex.objects.all()
    serializer_class = CourseIndexSerializer
    
class FacultyIndexViewSet(viewsets.ModelViewSet):
    queryset = FacultyIndex.objects.all()
    serializer_class = FacultyIndexSerializer
    
class StudentIndexViewSet(viewsets.ModelViewSet):
    queryset = StudentIndex.objects.all()
    serializer_class = StudentIndexSerializer

def login(request):
    return render(request,"login2.html")

class CourseGather(APIView):
    def get(self, request, year, semester, faculty_id):
        courseid = []
        coursename = []
        count = []
        val1 = []   #count,courseid,coursename
        print("Year:", year, "\nSemester : ",semester)  # Print the value to check if it matches the expected format.
        
        try:
            sem_obj = Semester.objects.get(sem = semester)
            print("\n\n",sem_obj)
            try:
                year_obj = Year.objects.get(year = year, sem=sem_obj)
                print("\n\n",year_obj)
                try:
                    facultyindex_obj = FacultyIndex.objects.get(faculty_id = faculty_id)
                    print("\n\n",facultyindex_obj)
                    try:
                        faculty_obj = Faculty.objects.filter(faculty = facultyindex_obj, faculty_year = year_obj)
                        print("\n\n",faculty_obj)
                        inc = 1
                        for faculty in faculty_obj:
                            course_id = faculty.course_id
                            courseindex_id = course_id.course
                            courseid.append(courseindex_id.course_id) 
                            coursename.append(courseindex_id.course_name)    
                            val1.append([inc,courseindex_id.course_id,courseindex_id.course_name])
                            count.append(inc)
                            inc+=1
                        print("\n\n\n",val1)
                        print("\n\n\n",courseid,"\n\n\n")
                        print("\n\n\n",coursename,"\n\n\n")
                    except Faculty.DoesNotExist:
                        print("Faculty object not found.")        
                except FacultyIndex.DoesNotExist:
                    print("Faculty Index object not found.")    
                #print("Year object:", year_obj)  # Print the retrieved year object.
            except Year.DoesNotExist:
                print("Year object not found.")    
        except Semester.DoesNotExist:
            print("Semester object not found.")
        
        response = HttpResponse("CourseGather Part")
        context  = {'data':val1, 'id' : courseid ,'name' : coursename,'count':count, 'datalen': len(courseid)} 
        print("\n\n",type(courseid))
        print(context)
        return render(request,"attendance_home.html",context)

class StudentGather(View):
    template_name = 'attendance.html'
    
    def __init__(self):
        self.val1=[]
        self.val2=[]
        
    def get(self, request, year, semester, faculty_id, course_id):
        studentroll = []
        studentname = []
        print("Year:", year, "\nSemester : ",semester)  # Print the value to check if it matches the expected format.
        
        try:
            sem_obj = Semester.objects.get(sem = semester)
            #print("\n\n",sem_obj)
            try:
                year_obj = Year.objects.get(year = year, sem=sem_obj)
                #print("\n\n",year_obj)     #year_id
                try:
                    facultyindex_obj = FacultyIndex.objects.get(faculty_id = faculty_id)
                    #print("\n\n",facultyindex_obj)    #fac_id
                    try:
                        courseindex_obj = CourseIndex.objects.get(course_id = course_id)
                        #print("\n\n",courseindex_obj)       #course_id 
                        try:
                            course_obj = Course.objects.get(course = courseindex_obj,course_year = year_obj)
                            #print("\n\n",course_obj)       #course_id 
                            try :
                                faculty_obj = Faculty.objects.get(faculty = facultyindex_obj, course_id=course_obj, faculty_year = year_obj)
                                #print("\n\n",faculty_obj)       #course_id 
                                try:
                                    student_obj = Student.objects.filter(course_id = faculty_obj, student_year = year_obj)
                                    #print("\n\n",student_obj)       #course_id 
                                    inc = 1
                                    for stud in student_obj:
                                        
                                        student_id = stud.student
                                        student_roll = student_id.student_id
                                        student_name = student_id.student_name
                                        self.val1.append([inc,student_roll, student_name])
                                        self.val2.append(inc)
                                        inc+=1
            
                                except Student.DoesNotExist:
                                    print("Faculty object not found.") 
                            except Faculty.DoesNotExist:
                                print("Faculty object not found.")
                        except Course.DoesNotExist:
                            print("Course object not found.")
                    except CourseIndex.DoesNotExist:
                        print("CourseIndex object not found.")        
                except FacultyIndex.DoesNotExist:
                    print("Faculty Index object not found.")    
                #print("Year object:", year_obj)  # Print the retrieved year object.
            except Year.DoesNotExist:
                print("Year object not found.")    
        except Semester.DoesNotExist:
            print("Semester object not found.")
        
        context  = { 'data' : self.val1 ,'data1' : self.val2, 'datalen': len(self.val1)} 
        
        print("\n\n",type(self.val1))
        print(context)
        
        
        return render(request,self.template_name,context)


def report(request):
    return render(request, 'report.html')

def home(request,faculty_id):
    return render(request, 'home.html')

def attendance(request):
    return render(request, 'attendance.html')


def my_ajax_view(request):
    if request.method == 'POST' :
        
        data = json.loads(request.body)
        
        semester = data[0][3]
        year = data[0][2]
        faculty_id = data[0][4]
        course_id = data[0][5]
        from_=data[1][0]
        to_=data[1][1]
        date_=data[1][2]
        att=data[2]
        
        print(semester,"\n\n")
        print(year,"\n\n")
        print(faculty_id,"\n\n")
        print(course_id,"\n\n")
        
        print(from_,"\n\n")
        print(to_,"\n\n")
        print(date_,"\n\n")
        print(att,"\n\n")
        print(type(att),"\n\n")
        # att = att[0][1:len(att)-1]
        print(att[0])
        print(len(att))
        att_ = []
        for i in range(0,len(att[0]),2):
            att_.append(int(att[0][i]))
        print("@ : ",att_)
        
        try:
            sem_obj = Semester.objects.get(sem = semester)
            #print("\n\n",sem_obj)
            try:
                year_obj = Year.objects.get(year = year, sem=sem_obj)
                #print("\n\n",year_obj)     #year_id
                try:
                    facultyindex_obj = FacultyIndex.objects.get(faculty_id = faculty_id)
                    #print("\n\n",facultyindex_obj)    #fac_id
                    try:
                        courseindex_obj = CourseIndex.objects.get(course_id = course_id)
                        #print("\n\n",courseindex_obj)       #course_id 
                        try:
                            course_obj = Course.objects.get(course = courseindex_obj,course_year = year_obj)
                            #print("\n\n",course_obj)       #course_id 
                            try :
                                faculty_obj = Faculty.objects.get(faculty = facultyindex_obj, course_id=course_obj, faculty_year = year_obj)
                                #print("\n\n",faculty_obj)       #course_id 
                                try:
                                    student_obj = Student.objects.filter(course_id = faculty_obj, student_year = year_obj)
                                    #print("\n\n",student_obj)       #course_id 
                                    for val in range(int(from_),int(to_)+1): 
                                        print(val)
                                        
                                        for stud,k in zip(student_obj,att_):
                                            
                                            if k == 1 :
                                                print(stud,val,"abs")
                                                attendance = Attendance(
                                                    student_detail = stud,
                                                    date = date_,
                                                    hrs = val,
                                                    status = "Absent"
                                                )
                                            elif k == 0:
                                                print(stud,val,"present")
                                                attendance = Attendance(
                                                    student_detail = stud,
                                                    date = date_,
                                                    hrs = val,
                                                    status = "Present"
                                                )
                                            attendance.save()
                                except Student.DoesNotExist:
                                    print("Faculty object not found.") 
                            except Faculty.DoesNotExist:
                                print("Faculty object not found.")
                        except Course.DoesNotExist:
                            print("Course object not found.")
                    except CourseIndex.DoesNotExist:
                        print("CourseIndex object not found.")        
                except FacultyIndex.DoesNotExist:
                    print("Faculty Index object not found.")    
                #print("Year object:", year_obj)  # Print the retrieved year object.
            except Year.DoesNotExist:
                print("Year object not found.")    
        except Semester.DoesNotExist:
            print("Semester object not found.")
        
        
            
        return JsonResponse({'status': 'success'})
        
        