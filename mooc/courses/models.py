from django.db import models

# Create your models here.

class Course(models.Model):

    name = models.CharField('Nome', max_length=100, blank=False, null=False)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição', blank=True)
    start_date = models.DateField('Data de início', null=True, blank=True)
    image = models.ImageField(upload_to='courses/images', verbose_name='Imagem')
    author = models.CharField('Autor', max_length=100)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    def return_name(self):
        return '%s %s' % (self.name)

    def __str__(self):
        return(self.name)

    def Meta(self):
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['name']

class CourseManager(models.Manager):
    
    def search(self, query):
        return self.get_queryset().filter(
        models.Q(name__icontains=query) | 
        models.Q(description__icontains=query)
        )