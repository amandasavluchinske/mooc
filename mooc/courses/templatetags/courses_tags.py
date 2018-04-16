""" from django.template import Library

register = Library()

from .courses.models import Enrollments

@register.inclusion_tag()
def my_courses(user):
    enrollments = Enrollments.objects.filter(user=user)
    context = {'enrollments': enrollments}
    return context """