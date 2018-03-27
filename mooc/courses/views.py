from django.shortcuts import render, get_object_or_404
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

class Details(DetailView):

    template_name = 'details.html'
    model = Course
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return (context)