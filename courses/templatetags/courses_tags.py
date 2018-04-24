from django import template
from django.template import Library
from courses.models import Enrollments
register = Library()

@register.filter
def my_courses(user):
    enrollments = Enrollments.objects.filter(user=user)
    context = {'enrollments': enrollments}
    return context

@register.assignment_tag
def load_my_courses(user):
    return Enrollments.objects.filter(user=user)