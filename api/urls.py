from django.urls import path
from .views import ProjectUpdateAPIView, ProjectDeleteAPIView, ProjectDetailAPIView

urlpatterns = [
    path('projects/<int:pk>/update/', ProjectUpdateAPIView.as_view()),
    path('projects/<int:pk>/delete/', ProjectDeleteAPIView.as_view()),
    path('projects/<int:pk>/detail/', ProjectDetailAPIView.as_view()),
]
