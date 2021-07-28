from django.shortcuts import render, get_object_or_404
from base.models import Project, UserGroup, TaskGroup
from django.core.exceptions import PermissionDenied
from .forms import TaskGroupForm


# Create your views here.

def index(request, id):
    user = request.user
    project = get_object_or_404(Project, id=id)
    # Присутствует ли пользователь в проекте
    if len(UserGroup.objects.filter(user_id=user.id, project_id=id)) == 0:
        raise PermissionDenied()

    command = [group.user for group in UserGroup.objects.filter(project_id=id)]

    groups = TaskGroup.objects.filter(project_id=id)

    taskgroupform = TaskGroupForm(initial={"Project": 1})

    data = {"user": user,
            "project": project,
            "command": command,
            "groups": groups,
            "TaskGroupForm": taskgroupform
            }
    return render(request, "project.html", data)
