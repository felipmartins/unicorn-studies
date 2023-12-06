from task_manager.models import Task
from django_unicorn.components import UnicornView


class TableView(UnicornView):
    books = Task.objects.none()

    def mount(self):
        self.load_table()

    def load_table(self):
        self.books = Task.objects.all()

        for child in self.children:
            if hasattr(child, "is_editing"):
                child.is_editing = False
