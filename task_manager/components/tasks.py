from django_unicorn.components import UnicornView
from task_manager.models import Task


class TasksView(UnicornView):
    books = Task.objects.none()

    def mount(self):
        self.books = Task.objects.all().order_by("-id")[:5]

    def save(self, book_idx: int):
        self.books[book_idx].save()
