from django import forms
from django.conf import settings
#from django.contrib.auth import get_user_model

#User = get_user_model()

'''class UserRegistration(forms.Form):
    username = forms.CharField(label='Usuário', max_length=100)
    e-mail = forms.CharField(label='Usuário', max_length=100)'''


class ContactCourse(forms.Form):
    
    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Mensagem', widget=forms.Textarea)

    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data)
        return cleaned_data

    """ def send_mail(self, course):
        subject = '[%s] - CONTATO' % course
        message = 'Nome: %(name)s;E-mail: %(email)s;%(message)s'
        context = {

            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'message': self.cleaned_data['message']

        }
        message = message % context
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_EMAIL]) """