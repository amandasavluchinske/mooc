from .models import Enrollments, Course
from users.models import User

def confirm_enrollment(user, course):
        return Enrollments.objects.filter(user=user, course=course).exists()