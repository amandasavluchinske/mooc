from django.db import models

class CourseManager(models.Manager):
    
    def search(self, query):
        return self.get_queryset().filter(
        models.Q(name__icontains=query) | 
        models.Q(description__icontains=query)
        )