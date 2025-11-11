from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path(r"", include("accounts.urls")),
    path("api/tasks/", include("task_manager.urls")),
]
