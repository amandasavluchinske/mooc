from .models import Enrollments, Course, Announcement
from django.shortcuts import get_object_or_404, render
from users.models import User
from .models import Announcement
from .forms import CommentAnnouncement

def confirm_enrollment(user, course):
        return Enrollments.objects.filter(user=user, course=course).exists()

def add_comment(request, pk):
        announcement = get_object_or_404(Announcement, pk=pk)
        if request.method == 'POST':
                form = CommentAnnouncement(request.POST)
                if form.is_valid():
                        comment = form.save(commit=False)
                        comment.user = self.request.user
                        comment.save()
                        return redirect('details', kwargs={'slug': self.kwargs['slug']})
                else:
                        form = CommentAnnouncement()
                return render(request, 'details', {'form': form})