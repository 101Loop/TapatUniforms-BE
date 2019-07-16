from django.contrib import admin

from .models import IndentRequestDetail, IndentRequest, Indent, BoxItem, Box

admin.site.register(Indent)
admin.site.register(IndentRequest)
admin.site.register(IndentRequestDetail)
admin.site.register(Box)
admin.site.register(BoxItem)
