from django.contrib import admin

from . import models

# Теперь данные модели можно редактировать в /admin
admin.site.register(models.Project)
admin.site.register(models.TaskGroup)
admin.site.register(models.Task)

#admin.site.register(models.UserGroup)


@admin.register(models.UserGroup)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("project", "user", "access")
    ordering = ["project"]
    list_filter = ["project", "user"]
