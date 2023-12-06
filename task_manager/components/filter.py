from django_unicorn.components import UnicornView
from task_manager.models import Task


class FilterView(UnicornView):
    search = ""

    def updated_search(self, query):
        self.parent.load_table()

        if query:
            self.parent.books = list(Task.objects.filter(title__contains=query)[0:10])
