from rest_framework import generics, permissions
from .models import Lead
from .serializers import LeadSerializer
from rest_framework import generics
from django.conf import settings
from .models import Lead
from .serializers import LeadSerializer
from .email_utils import send_email
from django.template.loader import render_to_string
from django.utils import timezone

class LeadCreateView(generics.CreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        lead = serializer.save()

        # 1️⃣ Send welcome email
        if lead.email:
            html = render_to_string(
    "emails/welcome.html",
    {
        "name": lead.full_name,
        "year": timezone.now().year,
        "logo_url": "https://streamsofjoysouthlondon.org/assets/images/email-logo.png",
        "directions_url": "https://www.google.com/maps/search/?api=1&query=51.4467903,-0.0197191",
        "whatsapp_url": "https://whatsapp.com/channel/0029VbCHgZV7dmeS4VRw9a0M",
    },
)

            try:
                send_email(
                    to_email=lead.email,
                    subject="You're In ✅ Streams of Joy South London",
                    html_content=html,
                )
            except Exception as e:
                print("User email failed:", e)

        # 2️⃣ Admin notification stays simple
        if getattr(settings, "ADMIN_NOTIFY_EMAIL", ""):
            try:
                send_email(
                    to_email=settings.ADMIN_NOTIFY_EMAIL,
                    subject="New signup received (SOJ South London)",
                    html_content=f"""
                        <strong>New Lead</strong><br><br>
                        Name: {lead.full_name}<br>
                        Email: {lead.email}<br>
                        Phone: {lead.phone}<br>
                        Source: {lead.source}
                    """,
                )
            except Exception as e:
                print("Admin email failed:", e)