from django.core.exceptions import PermissionDenied
from .models import Enrollments, Course
from users.models import User
from .helpers import confirm_enrollment
