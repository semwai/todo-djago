"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from base import views as base
from project import views as project


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base.index),
    path('login/', base.login, name='login'),
    path('project/<int:id>', project.index),
    path('taskgroup/<int:project_id>', project.task_group),
    path('task/<int:project_id>/<int:group_id>', project.task)
    # path('accounts/', include(urls))
]
