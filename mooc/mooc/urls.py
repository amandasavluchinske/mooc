from django.conf import settings
from django.conf.urls import include, url  # noqa
from django.contrib import admin
from django.views.generic import TemplateView, FormView, ListView

import django_js_reverse.views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^jsreverse/$', django_js_reverse.views.urls_js, name='js_reverse'),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^contact$', TemplateView.as_view(template_name='contact.html'), name='contact'),
    url(r'^cursos$', ListView.as_view(template_name='courses.html'), name='courses'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
