from django.conf import settings
from django.conf.urls import include, url  # noqa
from django.contrib import admin
from django.views.generic import TemplateView, FormView, ListView
from courses.views import Courses, Details, Enrollment, Announcements, Unrollment, ShowAnnouncement, Lessons, LessonDetail, ClassMaterial
from accounts.views import Login, Register, Logout, Dashboard, PasswordChange, PasswordChangeDone, EditAccount, PasswordReset, PasswordResetConfirm
from django.conf.urls.static import static

import django_js_reverse.views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^jsreverse/$', django_js_reverse.views.urls_js, name='js_reverse'),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^contact$', TemplateView.as_view(template_name='contact.html'), name='contact'),
    url(r'^cursos$', Courses.as_view(), name='courses'),
    #url(r'^cursos/(?P<pk>\d+)/$', Details.as_view(), name='details'),
    url(r'^cursos/(?P<slug>[\w-]+)/$', Details.as_view(), name='details'),
    url(r'^entrar/$', Login.as_view(), name='login'),
    url(r'^cadastro/$', Register.as_view(), name='register'),
    url(r'^/$', Logout.as_view(), name='logout'),
    url(r'^painel/$', Dashboard.as_view(), name='dashboard'),
    url(r'^editarsenha/$', PasswordChange.as_view(), name='passwordchange'),
    url(r'^editarsenha/concluido/$', PasswordChangeDone.as_view(), name='passwordchangedone'),
    url(r'^redefinirsenha/$', PasswordReset.as_view(), name='passwordreset'),
    url(r'^redefinirsenha/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', PasswordResetConfirm.as_view(), name='passwordresetconfirm'),
    url(r'^editarconta/$', EditAccount.as_view(), name='editaccount'),
    url(r'^cursos/(?P<slug>[\w-]+)/inscricao/$', Enrollment.as_view(), name='enrollment'),
    url(r'^(?P<slug>[\w-]+)/anuncios/$', Announcements.as_view(), name='announcements'),
    url(r'^(?P<slug>[\w-]+)/cancelar/$', Unrollment.as_view(), name='unrollment'),
    url(r'^(?P<slug>[\w-]+)/anuncios/(?P<pk>\d+)/$', ShowAnnouncement.as_view(), name='show_announcement'),
    url(r'^cursos/(?P<slug>[\w-]+)/aulas/(?P<pk>\d+)/$', LessonDetail.as_view(), name='lesson_detail'),
    url(r'^cursos/(?P<slug>[\w-]+)/aulas/$', Lessons.as_view(), name='lessons'),
    url(r'^cursos/(?P<slug>[\w-]+)/aulas/(?P<pk>\d+)/materiais/$', ClassMaterial.as_view(), name='materials'),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
