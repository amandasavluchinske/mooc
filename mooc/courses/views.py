from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, CourseManager, Enrollments
from .forms import ContactCourse
from django.views.generic import *
from django.contrib.auth.views import *
from django.views.generic.edit import FormMixin
from django.core.urlresolvers import reverse, reverse_lazy
from templated_email.generic_views import TemplatedEmailFormViewMixin
from templated_email import send_templated_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

# COURSES

class Courses(ListView):

    template_name = 'courses.html'
    model = Course
    context_object_name = 'courses'

    """ def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        return context """

class Details(FormMixin, DetailView):

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

        messages.success(self.request, 'Seu e-mail foi enviado!')

        message_content = form.cleaned_data.get('message')
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email'),

        send_templated_mail(
            template_name='template',
            from_email=email,
            recipient_list=['to@example.com'],
            context = {
                'name': name,
                'message_content': message_content
            }
        )
        return super().form_valid(form)

# TODO - MAKE THIS LOGINREQUIRED WORK!

class Enrollment(DetailView, LoginRequiredMixin):

    model = Enrollments
    template_name = 'index.html'

    def get_object(self):
	    course = get_object_or_404(Course, slug=self.kwargs['slug'])
	    return Enrollments.objects.get_or_create(user=self.request.user, course=course)

    def get_success_url(self):
        return reverse('dashboard')
    