from django.contrib import admin
from drfaddons.admin import CreateUpdateAdmin

from .models import School, Student


@admin.register(School)
class SchoolAdmin(CreateUpdateAdmin):
    list_display = ("id", "name", "city")
    search_fields = ("name", "city__name")
    list_filter = ("name", "city__name")
    ordering = ("id",)


@admin.register(Student)
class StudentAdmin(CreateUpdateAdmin):
    list_display = ("student_id", "name", "school")
    search_fields = ("student_id", "name", "school__name")
    list_filter = ["school__name"]


# admin.site.register(School, SchoolAdmin)
# admin.site.register(Student, StudentAdmin)
