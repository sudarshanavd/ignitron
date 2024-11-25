# account/urls.py
from django.urls import path
from django.contrib.auth import views
from .views import CustomLoginView



urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),  # Single login URL
    path("logout/", views.LogoutView.as_view(), name="logout"),
]
