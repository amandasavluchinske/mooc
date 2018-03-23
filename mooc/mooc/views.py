from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import *
from .models import *
#DetailView, FormView, TemplateView, UpdateView, ListView

class Home(TemplateView):
    template_name = 'home.html'

    def get_success_url(self):
        return reverse('home')

class Contact(TemplateView):
    template_name = 'contact.html'


    def get_success_url(self):
        return reverse('contact')