from django.contrib import admin
from drfaddons.admin import CreateUpdateAdmin
from .models import School, Student


class SchoolAdmin(CreateUpdateAdmin):
    list_display = ("id", "name", "city")
    search_fields = list_display
    ordering = ("id",)


class StudentAdmin(CreateUpdateAdmin):
    list_display = ("student_id", "name", "school")
    search_fields = list_display


admin.site.register(School, SchoolAdmin)
admin.site.register(Student, StudentAdmin)
