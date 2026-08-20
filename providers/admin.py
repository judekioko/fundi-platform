from django.contrib import admin

from .models import Provider


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ["business_name", "category", "area", "phone", "is_approved", "created_at"]
    list_filter = ["category", "is_approved"]
    list_editable = ["is_approved"]
    search_fields = ["business_name", "phone", "area", "user__email"]
