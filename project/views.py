from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from base.models import Project, UserGroup, TaskGroup
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from .forms import TaskGroupForm


# Create your views here.
@login_required(login_url='login')
def index(request, id):
    user = request.user
    project = get_object_or_404(Project, id=id)
    # Присутствует ли пользователь в проекте
    if len(UserGroup.objects.filter(user_id=user.id, project_id=id)) == 0:
        raise PermissionDenied()

    command = [group.user for group in UserGroup.objects.filter(project_id=id)]

    groups = TaskGroup.objects.filter(project_id=id)

    data = {"user": user,
            "project": project,
            "command": command,
            "groups": groups,
            }

    return render(request, "project.html", data)


@login_required(login_url='login')
def task_group(request, project_id):
    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        task = TaskGroup.objects.create(name=name, description=description, project_id=project_id)
        task.save()
        return HttpResponse("OK, <a href=/project/%s>back</a>" % project_id)
    else:
        form = TaskGroupForm(initial={"Project": project_id})
        data = {"TaskGroupForm": form}
        return render(request, "taskgroup.html", data)


@login_required(login_url='login')
def task(request, project_id, group_id):
    if request.method == "POST":
        pass
    else:
        pass