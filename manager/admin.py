from django.contrib import admin
from drfaddons.admin import CreateUpdateAdmin
from .models import Manager


@admin.register(Manager)
class ManagerAdmin(CreateUpdateAdmin):
    list_display = ("id", "outlet", "user")
    search_fields = ["user__name"]
    ordering = ["id"]
