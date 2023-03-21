from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import redirect
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks = Task.objects.filter(is_finished=False)
        context['tasks'] = tasks
        return context


class TaskDetailView(DetailView):
    template_name = 'task_view.html'
    model = Task
    context_object_name = 'task'


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task_list')


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    context_object_name = 'task'
    success_url = reverse_lazy('task_list')


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'task_confirm_delete.html'
    success_url = reverse_lazy('task_list')

    def get_success_url(self):
        next_url = self.request.POST.get('next', None)
        if next_url:
            return next_url
        else:
            return reverse_lazy('task_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())


class TaskDeleteSelectedView(LoginRequiredMixin, View):
    def post(self, request):
        selected_tasks = request.POST.getlist('selected_tasks')
        Task.objects.filter(pk__in=selected_tasks).update(is_finished=True)
        return redirect('task_list')


class ProjectListView(ListView):
    model = Project
    template_name = 'project/project_list.html'
    context_object_name = 'projects'
    ordering = 'start_date'
    paginate_by = 5

    def get_queryset(self):
        return Project.objects.filter(is_deleted=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for project in context['projects']:
            project.filtered_tasks = project.tasks.filter(is_finished=False)
        return context


class ProjectDetailView(DetailView):
    template_name = 'project/project_view.html'
    model = Project
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = context['project']
        filtered_tasks = project.tasks.filter(is_finished=False)
        context['filtered_tasks'] = filtered_tasks
        return context


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project/project_form.html'
    success_url = reverse_lazy('project_list')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        response = super().form_valid(form)
        form.instance.members.add(self.request.user)
        return response


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project/project_form.html'
    success_url = reverse_lazy('project_list')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def dispatch(self, request, *args, **kwargs):
        project = self.get_object()

        if project.creator != self.request.user:
            return HttpResponseForbidden('You are not allowed to update this project.')

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        return super().form_valid(form)


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'project/project_confirm_delete.html'
    success_url = reverse_lazy('project_list')

    def dispatch(self, request, *args, **kwargs):
        project = self.get_object()

        if project.creator != self.request.user:
            return HttpResponseForbidden('You are not allowed to delete this project.')

        return super().dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())


class ProjectDeleteSelectedView(LoginRequiredMixin, View):
    def post(self, request):
        selected_projects = request.POST.getlist('selected_projects')
        Project.objects.filter(pk__in=selected_projects).delete()
        return redirect('project_list')


class SearchView(ListView):
    model = Project
    template_name = 'project/search_results.html'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Project.objects.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query)
            )
        return Project.objects.none()
