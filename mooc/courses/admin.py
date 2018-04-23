from django.contrib import admin
from .models import Course, Enrollments, Announcement, Comment, Lesson, Material

class CourseAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'start_date', 'created_at', 'author']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class EnrollmentsAdmin(admin.ModelAdmin):

    list_display = ['user', 'course', 'start_date', 'created_at', 'status']
    search_fields = ['user', 'course']


class MaterialInlineAdmin(admin.StackedInline):

    model = Material


class LessonAdmin(admin.ModelAdmin):

    list_display = ['name', 'number', 'course', 'release_date']
    search_fields = ['name', 'description']
    list_filter = ['created_at']

    inlines = [MaterialInlineAdmin]

admin.site.register(Course, CourseAdmin)
admin.site.register(Enrollments)
admin.site.register(Announcement)
admin.site.register(Comment)
admin.site.register(Lesson, LessonAdmin)