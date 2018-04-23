from .models import Enrollments, Course, Announcement
from django.shortcuts import get_object_or_404, render
from users.models import User
from .models import Announcement
from .forms import CommentAnnouncement

def confirm_enrollment(user, course):
        return Enrollments.objects.filter(user=user, course=course).exists()