from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils.datetime_safe import datetime
from django.views.decorators.csrf import csrf_exempt

from base.models import Project, UserGroup, TaskGroup, Task
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from .forms import TaskGroupForm, TaskForm


# Create your views here.
@login_required(login_url='login')
def index(request, id):
    user = request.user
    project = get_object_or_404(Project, id=id)
    # Присутствует ли пользователь в проекте
    if len(UserGroup.objects.filter(user_id=user.id, project_id=id)) == 0:
        raise PermissionDenied()
    command = [group.user for group in UserGroup.objects.filter(project_id=id)]
    tasks = Task.objects.filter(group__project_id=id)
    # Те группы, у которых нет своих задач
    empty_groups = TaskGroup.objects\
        .filter(project__id=2)\
        .exclude(id__in=[task.group_id for task in Task.objects.all()])
    data = {"user": user,
            "project": project,
            "command": command,
            "tasks": tasks,
            "empty_groups": empty_groups
            }

    return render(request, "project.html", data)


@login_required(login_url='login')
def task_group(request, project_id):
    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        task = TaskGroup.objects.create(
            name=name,
            description=description,
            project_id=project_id
        )
        task.save()
        return HttpResponse("OK, <a href=/project/%s>back</a>" % project_id)
    else:
        form = TaskGroupForm(initial={"Project": project_id})
        data = {"TaskGroupForm": form}
        return render(request, "taskgroup.html", data)


@login_required(login_url='login')
def task(request, project_id, group_id):
    if request.method == "POST":
        name = request.POST['name']
        text = request.POST['text']
        create_date = datetime.now()
        author = request.user.id
        task = Task.objects.create(
            name=name,
            text=text,
            create_date=create_date,
            author_id=author,
            group_id=group_id
        )
        return HttpResponse("OK, <a href=/project/%s>back</a>" % project_id)
    else:
        form = TaskForm()
        return render(request, "task.html", {"form": form})