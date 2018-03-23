from django.shortcuts import render
from .models import Course, CourseManager
from django.views.generic import *

# Create your views here.

class Courses(ListView):

    template_name = 'courses.html'
    model = Course

    def get_context_data(self, **kwargs):
        for course in Course.objects.get(name):
            context = Course.objects.get(name)
            return context