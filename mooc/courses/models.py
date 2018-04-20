from django.db import models
from django.core.urlresolvers import reverse
from users.models import User
from django.conf import settings


class Course(models.Model):

    name = models.CharField('Nome', max_length=100, blank=False, null=False)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição', blank=True)
    about = models.TextField('Sobre o curso', blank=True)
    start_date = models.DateField('Data de início', null=True, blank=True)
    image = models.ImageField(upload_to='courses/images', verbose_name='Imagem', blank=True)
    author = models.CharField('Autor', max_length=100)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    # TODO: Need to remember what this is
    def return_name(self):
        return '%s %s' % (self.name)

    def __str__(self):
        return(self.name)

    def Meta(self):
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('details', kwargs={'slug': self.slug})


class CourseManager(models.Manager):
    
    def search(self, query):
        return self.get_queryset().filter(
        models.Q(name__icontains=query) | 
        models.Q(description__icontains=query)
        )

class Enrollments(models.Model):

    STATUS_CHOICES=(
        (0, 'Pendente'),
        (1, 'Aprovado'),
        (2, 'Cancelado'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuário', related_name='enrollments')
    course = models.ForeignKey(Course, verbose_name='Curso', related_name='enrollments')
    status = models.IntegerField('Situação', choices=STATUS_CHOICES, default=1)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    """ def active(self):
        self.status = 1
        self.save()

    def inactive(self):
        self.status = 2
        self.save()
 """
    class Meta:
        verbose_name='Inscrição'
        verbose_name_plural='Inscrições'
        unique_together = (('user', 'course'),)

    objects = models.Manager()

class Announcement(models.Model):

    course = models.ForeignKey(Course, verbose_name='Curso')
    title = models.CharField('Título', max_length=100)
    content = models.TextField('Conteúdo')
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Anúncio'
        verbose_name_plural='Anúncios'
        ordering=['-created_at']

class Comment(models.Model):
    
    announcement = models.ForeignKey(Announcement, verbose_name='Anúncio', related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuário', related_name='comments')
    comment = models.TextField('Comentário')
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name='Comentário'
        verbose_name_plural='Comentários'
        ordering=['created_at']