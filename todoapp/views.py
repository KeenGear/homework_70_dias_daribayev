from django.core.exceptions import ValidationError
from django.db.models import Q
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Task, Project
from .forms import TaskForm, ProjectForm


class TaskListView(ListView):
    template_name = 'task_list.html'
    model = Task
    context_object_name = 'tasks'
    ordering = 'updated_at'
    paginate_by = 5


class TaskDetailView(DetailView):
    template_name = 'task_view.html'
    model = Task
    context_object_name = 'task'


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task_list')


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    context_object_name = 'task'
    success_url = reverse_lazy('task_list')


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_confirm_delete.html'
    success_url = reverse_lazy('task_list')

    def get_success_url(self):
        next_url = self.request.POST.get('next', None)
        if next_url:
            return next_url
        else:
            return reverse_lazy('task_list')


class TaskDeleteSelectedView(View):
    def post(self, request):
        selected_tasks = request.POST.getlist('selected_tasks')
        Task.objects.filter(pk__in=selected_tasks).delete()
        return redirect('task_list')


class ProjectListView(ListView):
    model = Project
    template_name = 'project/project_list.html'
    context_object_name = 'projects'
    ordering = 'start_date'
    paginate_by = 5


class ProjectDetailView(DetailView):
    template_name = 'project/projetc_view.html'
    model = Project
    context_object_name = 'project'


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project/project_form.html'
    success_url = reverse_lazy('project_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context


class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project/project_form.html'
    success_url = reverse_lazy('project_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(instance=self.object)
        return context


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'project/project_confirm_delete.html'
    success_url = reverse_lazy('project_list')


class ProjectDeleteSelectedView(View):
    def post(self, request):
        selected_projects = request.POST.getlist('selected_projects')
        Project.objects.filter(pk__in=selected_projects).delete()
        return redirect('project_list')
