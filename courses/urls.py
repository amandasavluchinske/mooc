from django.conf import settings
from django.conf.urls import include, url  # noqa
from django.contrib import admin
from django.views.generic import TemplateView, FormView

import django_js_reverse.views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
]