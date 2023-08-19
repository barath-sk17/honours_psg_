from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from record.views import SemesterViewSet, YearViewSet, CourseViewSet, \
    FacultyViewSet, StudentViewSet, AttendanceViewSet, CourseIndexViewSet, \
    StudentIndexViewSet, FacultyIndexViewSet, CourseGather, StudentGather, \
    my_ajax_view, login, report, home ,attendance





router = routers.DefaultRouter()
router.register(r'semester', SemesterViewSet, basename='semester')
router.register(r'year', YearViewSet, basename='year')
router.register(r'course_index', CourseIndexViewSet, basename='course_index')
router.register(r'course', CourseViewSet, basename='course')
router.register(r'faculty_index', FacultyIndexViewSet, basename='faculty_index')
router.register(r'faculty', FacultyViewSet, basename='faculty')
router.register(r'student_index', StudentIndexViewSet, basename='student_index')
router.register(r'student', StudentViewSet, basename='student')
router.register(r'attendance', AttendanceViewSet, basename='attendance')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('login/',login, name="login"),
    #path('my-view/', my_ajax_view, name='my_ajax_view'),
    #path('demo/',demo, name='demo'),
    path('my_ajax_view/',my_ajax_view, name='my_ajax_view'),
    #path('attendcheck/<str:year>/<str:semester>/<str:faculty_id>/<str:course_id>/', my_ajax_view, name='my_ajax_view'),
    path('check/<str:year>/<str:semester>/<str:faculty_id>', CourseGather.as_view()),
    
    path('report/',report, name='report'),
    path('home/<str:faculty_id>',home, name='home'),
    path('attendance/',attendance, name='attendance'),
    path('check/<str:year>/<str:semester>/<str:faculty_id>/<str:course_id>', StudentGather.as_view()),
]
