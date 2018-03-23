from django.shortcuts import render
from .models import Course, CourseManager
from django.views.generic import *

# Create your views here.

class Courses(TemplateView):

    template_name = 'courses.html'
    model = Course
    context_object_name = 'courses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        return context