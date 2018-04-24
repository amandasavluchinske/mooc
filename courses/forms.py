from django import forms
from django.forms import ModelForm
from django.conf import settings
from users.models import User
from .models import Comment
from django.contrib.auth.forms import PasswordResetForm
from templated_email import send_templated_mail

class ContactCourse(forms.Form):
    
    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Mensagem', widget=forms.Textarea)

    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data)
        return cleaned_data

class CommentAnnouncement(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment']

    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data)
        return cleaned_data