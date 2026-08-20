from django.contrib import admin

from .models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ["category", "name", "location", "urgency", "matched_provider", "created_at"]
    list_filter = ["category", "urgency"]
    search_fields = ["name", "phone", "location", "description"]
