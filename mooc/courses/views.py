from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, CourseManager
from .forms import ContactCourse
from django.views.generic import *
from django.contrib.auth.views import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse, reverse_lazy
from templated_email.generic_views import TemplatedEmailFormViewMixin
from templated_email import send_templated_mail
from django.contrib.auth import get_user_model, REDIRECT_FIELD_NAME


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
        #form.save()
        #form.send_email(course)
        send_templated_mail(
            template_name='template',
            from_email='from@example.com',
            recipient_list=['to@example.com'],
            context = {}
            # Optional:
            # cc=['cc@example.com'],
            # bcc=['bcc@example.com'],
            # headers={'My-Custom-Header':'Custom Value'},
            # template_prefix="my_emails/",
            # template_suffix="email",
        )
        return super(Details, self).form_valid(form)


# AUTHENTICATION
    
class Login(LoginView):

    template_name = 'login.html'
    success_url = reverse_lazy('dashboard')
    redirect_authenticated_user = True

    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('dashboard'))
        return super(Login, self).get(request)


class Register(FormView):
    form_class = UserCreationForm
    template_name = 'register.html'
    User = get_user_model()
    redirect_authenticated_user = True

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return redirect('home')


class Logout(LogoutView):
    next_page = 'home'  


class PasswordChange(PasswordChangeView):
    template_name = 'passwordchange.html'
    success_url = reverse_lazy('passwordchangedone')

class PasswordChangeDone(PasswordChangeDoneView):
    template_name = 'passwordchangedone.html'

# USERFEATURES

class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'
    model = Course
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cursos'] = Course.objects.all()
        return (context)

