from django.contrib import admin
from .models import Tag, Task, Project

# Register your models here.
admin.site.register(Tag)
admin.site.register(Task)
admin.site.register(Project)
