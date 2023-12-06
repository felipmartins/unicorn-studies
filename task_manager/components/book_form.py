from django_unicorn.components import UnicornView
from django import forms


class BookForm(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    publish_date = forms.DateField(required=True)


class BookFormView(UnicornView):
    form_class = BookForm

    title = ""
    publish_date = ""
