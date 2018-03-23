from django.contrib import admin
from .models import Course
# Register your models here.

class CourseAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'start_date', 'created_at', 'author']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Course, CourseAdmin)