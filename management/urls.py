from django.urls import path
from management.views.student_profile import StudentProfile

urlpatterns = [
    path('student-profile/', StudentProfile.as_view(), name='student_profile')
]