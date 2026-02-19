from django.contrib import admin
from .models import Lead

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "interest", "created_at")
    search_fields = ("full_name", "email", "phone")
    list_filter = ("interest", "created_at")