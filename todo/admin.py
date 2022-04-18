from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',) # чтобы дата в панели админа была нередактируемой

admin.site.register(Todo, TodoAdmin)
