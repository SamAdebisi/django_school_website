from django.contrib import admin

from .models import Course, Instructor


class InstructorInline(admin.TabularInline):
    model = Instructor


class CourseAdmin(admin.ModelAdmin):
    inlines = [
        InstructorInline,
    ]
    list_display = (
        'name', 'track', 'discount_price',
    )


admin.site.register(Course, CourseAdmin)
