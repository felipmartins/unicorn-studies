from django.urls import path
from task_manager.views import index

urlpatterns = [
    path("", index, name="home-page"),
]
