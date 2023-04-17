from django.urls import path
from .views import LoginView, logout_view, signup, ProfileView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('registration/', signup, name='registration'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
]
