from django.contrib import admin
from .models import Course, Enrollments
# Register your models here.

class CourseAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'start_date', 'created_at', 'author']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

class EnrollmentsAdmin(admin.ModelAdmin):

    list_display = ['user', 'course', 'start_date', 'created_at', 'status']
    search_fields = ['user', 'course']

admin.site.register(Course, CourseAdmin)
admin.site.register(Enrollments)