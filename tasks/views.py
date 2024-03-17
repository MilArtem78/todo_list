from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic, View

from tasks.forms import TaskCreateForm, TaskContentSearchForm
from tasks.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")
    template_name = "tasks/index.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)

        content = self.request.GET.get("content", "")

        context["search_form"] = TaskContentSearchForm(initial={"content": content})
        return context

    def get_queryset(self):
        form = TaskContentSearchForm(self.request.GET)
        if form.is_valid():
            return (
                super()
                .get_queryset()
                .filter(content__icontains=form.cleaned_data["content"])
            )


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy("todo-app:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy("todo-app:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo-app:index")


