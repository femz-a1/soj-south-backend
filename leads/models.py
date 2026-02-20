from django.db import models

class Lead(models.Model):
    full_name = models.CharField(max_length=120, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)

    # preferences (your checkboxes)
    wants_launch_updates = models.BooleanField(default=False)
    wants_sunday_reminders = models.BooleanField(default=False)
    wants_event_notifications = models.BooleanField(default=False)
    wants_whatsapp = models.BooleanField(default=False)
    wants_to_volunteer = models.BooleanField(default=False)
    is_newcomer = models.BooleanField(default=False)
    consent = models.BooleanField(default=False)

    # helpful for footer signups
    source = models.CharField(max_length=30, blank=True)  # "footer", "modal", etc.

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email