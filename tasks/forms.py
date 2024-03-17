from django import forms
from django.forms import DateTimeInput
from django.utils import timezone

from tasks.models import Task, Tag


class TaskCreateForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        widget=DateTimeInput(attrs={"type": "datetime-local"}),
        initial=timezone.now().replace(second=0, microsecond=0),
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Task
        fields = "__all__"


class TaskContentSearchForm(forms.Form):
    content = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by content"}),
    )
