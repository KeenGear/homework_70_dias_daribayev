from django.shortcuts import redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView
from .models import Task
from .forms import TaskForm


class TaskListView(TemplateView):
    template_name = 'task_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context


class TaskDetailView(TemplateView):
    template_name = 'task_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = Task.objects.get(pk=self.kwargs['pk'])
        return context


class TaskCreateView(TemplateView):
    template_name = 'task_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TaskForm()
        return context

    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect('task_detail', pk=task.pk)
        else:
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)


class TaskUpdateView(TemplateView):
    template_name = 'task_form.html'

    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(instance=task)
        return self.render_to_response({'form': form})

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            return redirect('task_detail', pk=task.pk)
        return self.render_to_response({'form': form})


class TaskDeleteView(TemplateView):
    template_name = 'task_confirm_delete.html'

    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        return self.render_to_response({'task': task})

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect('task_list')


class TaskDeleteSelectedView(View):
    def post(self, request):
        selected_tasks = request.POST.getlist('selected_tasks')
        Task.objects.filter(pk__in=selected_tasks).delete()
        return redirect('task_list')
