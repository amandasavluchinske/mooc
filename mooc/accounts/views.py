from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import auth
from django.views.generic import *
from django.contrib.auth.views import *
from django.contrib.auth import authenticate
from .forms import UserForm, EditAccount, PasswordReset, PasswordResetConfirm
from courses.models import Course, Enrollments
from courses.managers import CourseManager
from users.models import User
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse, reverse_lazy
from templated_email.generic_views import TemplatedEmailFormViewMixin
from templated_email import send_templated_mail
from django.contrib.auth import REDIRECT_FIELD_NAME, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin


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
    form_class = UserForm
    template_name = 'register.html'
    model = get_user_model()
    redirect_authenticated_user = True

    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('home'))
        return super(Register, self).get(request)


    def form_valid(self, form):
        raw_password = form.cleaned_data.get('password')
        self.object = form.save(commit=False)
        self.object.set_password(raw_password)
        self.object.save()
        user = authenticate(username=self.object.email, password=raw_password)
        login(self.request, user)
        return redirect('home')

class EditAccount(UpdateView, LoginRequiredMixin, SuccessMessageMixin):
    template_name = 'edit.html'
    model = User
    fields = ['name', 'email']

    success_message = 'Você alterou as suas informações com sucesso!'

    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)

class Logout(LogoutView):
    next_page = 'home'  

# Change Password

class PasswordChange(LoginRequiredMixin, PasswordChangeView):
    template_name = 'passwordchange.html'
    success_url = reverse_lazy('passwordchangedone')

class PasswordChangeDone(LoginRequiredMixin, PasswordChangeDoneView):
    template_name = 'passwordchangedone.html'

# Reset Password

class PasswordReset(PasswordResetView):
    form_class = PasswordReset
    template_name = 'registration/password_reset.html'
    email_template_name = 'password_reset_email'
    success_url = reverse_lazy('passwordreset')
    from_email = settings.DEFAULT_FROM_EMAIL

    def form_valid(self, form):
        print(self)
        return super().form_valid(form)

class PasswordResetConfirm(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'
    success_url = reverse_lazy('dashboard')
    form_class = PasswordResetConfirm

# USER FEATURES

class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'
    model = Course
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['enrollments'] = Enrollments.objects.filter(user=self.request.user)
        return (context)

