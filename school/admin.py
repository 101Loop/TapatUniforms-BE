from django.contrib import admin
from drfaddons.admin import CreateUpdateAdmin
from .models import School, Student


class SchoolAdmin(CreateUpdateAdmin):
    list_display = ('name', )
    search_fields = list_display


class StudentAdmin(CreateUpdateAdmin):
    list_display = ('id_no', 'name', 'school')
    search_fields = list_display


admin.site.register(School, SchoolAdmin)
admin.site.register(Student, StudentAdmin)
