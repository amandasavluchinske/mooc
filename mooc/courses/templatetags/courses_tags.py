from django import template
from django.template import Library
from courses.models import Enrollments
register = Library()

@register.inclusion_tag('../templates/my_courses.html')
def my_courses(user):
    enrollments = Enrollments.objects.filter(user=user)
    context = {'enrollments': enrollments}
    return context

@register.assignment_tag
def load_my_courses(user):
    return Enrollments.objects.filter(user=user)