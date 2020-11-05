from django.shortcuts import render, HttpResponse
from django.views import View
# Create your views here.

class StudentProfile(View):
    def get(self, request):
        return render(request, 'student_signup.html')