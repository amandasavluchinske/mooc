from django import forms
from django.forms import ModelForm
from django.conf import settings
from users.models import User

#User = get_user_model()

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
                "password and confirm_password does not match"
            )


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