from rest_framework import serializers
from .models import Lead

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = [
            "id",
            "full_name",
            "email",
            "phone",
            "wants_launch_updates",
            "wants_sunday_reminders",
            "wants_event_notifications",
            "wants_whatsapp",
            "wants_to_volunteer",
            "is_newcomer",
            "consent",
            "source",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]