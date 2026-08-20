from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.landing, name="landing"),
    path("requests/<int:job_id>/thanks/", views.job_thanks, name="job_thanks"),
]
