from django.urls import path
from .views import TaskCreateView, TaskUpdateView, TaskDeleteView, TaskListView, TaskDeleteSelectedView, TaskDetailView

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('tasks/create/', TaskCreateView.as_view(), name='task_create'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('tasks/delete_selected/', TaskDeleteSelectedView.as_view(), name='task_delete_selected'),
]
