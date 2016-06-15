from django.contrib import admin
from .models import Department, Item


class DepartmentAdmin(admin.ModelAdmin):
    pass


class ItemAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['usage', 'department']}),
        ('Pc information', {'fields': ['cpu', 'board', 'mem', 'disk', 'display']}),
        ('Description', {'fields': ['history_usage', 'description']}),
    ]
    list_display = ['usage', 'department', 'cpu', 'board', 'mem', 'disk', 'display', 'up_time', 'history_usage']
    list_filter = ['department', 'cpu', 'up_time']
    search_fields = ['usage', 'department', 'cpu', 'board', 'mem', 'disk', 'display', 'history_usage']

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Item, ItemAdmin)
