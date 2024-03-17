from django.contrib import admin

from tasks.models import Tag, Task

admin.site.register(Tag)
admin.site.register(Task)
