from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, CourseManager
from .forms import ContactCourse
from django.views.generic import *
from django.views.generic.edit import FormMixin
from django.core.urlresolvers import reverse, reverse_lazy
from templated_email.generic_views import TemplatedEmailFormViewMixin

# Create your views here.

class Courses(TemplateView):

    template_name = 'courses.html'
    model = Course
    context_object_name = 'courses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        return context

class Details(FormMixin, TemplatedEmailFormViewMixin, DetailView):

    template_name = 'details.html'
    model = Course
    context_object_name = 'course'
    form_class = ContactCourse

    def get_success_url(self):
        return reverse_lazy('details', kwargs={'slug': self.kwargs['slug']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ContactCourse
        return (context)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        #form.save()
        form.send_email(course)
        return super(Details, self).form_valid(form)
    
    