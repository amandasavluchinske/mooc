from django import forms
from django.forms import ModelForm
from django.conf import settings
from users.models import User
from django.contrib.auth.forms import PasswordResetForm
from templated_email import send_templated_mail

class UserForm(ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['name', 'email', 'password']

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "As senhas não são iguais!"
            )

class PasswordReset(PasswordResetForm):

    def send_mail(self, subject_template_name, email_template_name,
                  context, from_email, to_email, html_email_template_name=None):
        send_templated_mail(
            template_name=email_template_name,
            from_email=from_email,
            recipient_list=[to_email],
            context=context
        )

class PasswordResetConfirm(PasswordResetForm):
    pass

class EditAccount(ModelForm):

    class Meta:
        model = User
        fields = ['name', 'email']
