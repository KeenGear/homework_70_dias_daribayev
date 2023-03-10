from django.urls import path
from .views import TaskCreateView, TaskUpdateView, TaskDeleteView, TaskListView, TaskDeleteSelectedView, TaskDetailView, \
    ProjectListView, ProjectCreateView, ProjectDeleteView, ProjectUpdateView, ProjectDeleteSelectedView, SearchView

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('tasks/create/', TaskCreateView.as_view(), name='task_create'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('tasks/delete_selected/', TaskDeleteSelectedView.as_view(), name='task_delete_selected'),
    path('projects/', ProjectListView.as_view(), name='project_list'),
    path('projects/create/', ProjectCreateView.as_view(), name='project_create'),
    path('projects/<int:pk>/update/', ProjectUpdateView.as_view(), name='project_update'),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    path('projects/delete_selected/', ProjectDeleteSelectedView.as_view(), name='project_delete_selected'),
    path('search/', SearchView.as_view(), name='search'),
]
