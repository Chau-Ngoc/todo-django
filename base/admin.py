from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("score", "write", "speak", "listen")
    list_filter = ("fulfilled", "user")


# Register your models here.
admin.site.register(Task, TaskAdmin)
