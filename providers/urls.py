from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = "providers"

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="providers/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("jobs/<int:job_id>/claim/", views.claim_job, name="claim_job"),
]
