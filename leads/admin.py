from django.contrib import admin
from .models import Lead

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("email", "full_name", "phone", "source", "created_at")
    search_fields = ("full_name", "email", "phone")
    list_filter = ("source", "wants_to_volunteer", "is_newcomer", "created_at")