from rest_framework import generics, permissions
from .models import Lead
from .serializers import LeadSerializer
from rest_framework import generics
from django.conf import settings
from .models import Lead
from .serializers import LeadSerializer
from .email_utils import send_email

class LeadCreateView(generics.CreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    permission_classes = [permissions.AllowAny]
    
    def perform_create(self, serializer):
        lead = serializer.save()

        # 1) Email the person (if they provided email)
        if lead.email:
            send_email(
                to_email=lead.email,
                subject="You’re in ✅ Streams of Joy South London",
                html_content=f"""
                    <p>Hi {lead.full_name or "there"},</p>
                    <p>Thanks for signing up. We’ll keep you updated about services and announcements.</p>
                    <p><strong>Streams of Joy South London</strong></p>
                """,
            )

        # 2) Notify your team
        if getattr(settings, "ADMIN_NOTIFY_EMAIL", ""):
            send_email(
                to_email=settings.ADMIN_NOTIFY_EMAIL,
                subject="New signup received (SOJ South London)",
                html_content=f"""
                    <p><strong>New lead</strong></p>
                    <ul>
                      <li>Name: {lead.full_name}</li>
                      <li>Email: {lead.email}</li>
                      <li>Phone: {lead.phone}</li>
                      <li>Source: {lead.source}</li>
                      <li>Launch updates: {lead.wants_launch_updates}</li>
                      <li>Sunday reminders: {lead.wants_sunday_reminders}</li>
                      <li>Events: {lead.wants_event_notifications}</li>
                      <li>WhatsApp: {lead.wants_whatsapp}</li>
                      <li>Volunteer: {lead.wants_to_volunteer}</li>
                      <li>Newcomer: {lead.is_newcomer}</li>
                    </ul>
                """,
            )