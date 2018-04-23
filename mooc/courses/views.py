from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Enrollments, Announcement, Comment
from .managers import CourseManager
from .forms import ContactCourse, CommentAnnouncement
from .helpers import confirm_enrollment
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
        email = form.cleaned_data.get('email')

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

class Enrollment(LoginRequiredMixin, DetailView):

    model = Enrollments
    template_name = 'index.html'

    def get_object(self):
	    course = get_object_or_404(Course, slug=self.kwargs['slug'])
	    return Enrollments.objects.get_or_create(user=self.request.user, course=course)

    def get_success_url(self):
        return reverse('dashboard')
    
class Announcements(LoginRequiredMixin, DetailView):

    model = Course
    template_name = 'announcements.html'

    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        course = self.get_object()
        if not confirm_enrollment(user=user, course=course):
            return HttpResponseRedirect(reverse('dashboard'))
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['announcements'] = Announcement.objects.filter(course=self.get_object())
        return (context)


class ShowAnnouncement(LoginRequiredMixin, FormMixin, DetailView):

    model = Announcement
    template_name = 'announcement.html'
    context_object_name = 'announcement'
    form_class = CommentAnnouncement

    def get_success_url(self):
        return reverse_lazy('show_announcement', kwargs={'slug': self.kwargs['slug'], 'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        announcement = self.get_object()
        comments = Comment.objects.filter(announcement=announcement)
        context['comments'] = comments
        context['form'] = CommentAnnouncement
        return (context)


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):

        messages.success(self.request, 'Seu comentário foi postado!')

        user = self.request.user
        comment = form.cleaned_data.get('comment')
        announcement = self.get_object()
        post = Comment.objects.create(comment=comment, user=user, announcement=announcement)
        
        return super().form_valid(form)
        


class Unrollment(LoginRequiredMixin, DeleteView):

    template_name = 'undo_enrollment.html'
    model = Enrollments

    def get_object(self):
        return get_object_or_404(Enrollments, user=self.request.user, course__slug=self.kwargs['slug'])

    def get_success_url(self):
        messages.success(self.request, 'Você cancelou a sua inscrição com sucesso.')
        return reverse_lazy('dashboard')