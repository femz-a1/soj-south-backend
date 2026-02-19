from django.db import models

class Lead(models.Model):
    INTEREST_CHOICES = [
        ("member", "I want to join"),
        ("volunteer", "I want to volunteer"),
        ("partner", "I want to partner"),
        ("other", "Other"),
    ]

    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    interest = models.CharField(max_length=20, choices=INTEREST_CHOICES, default="member")
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} ({self.interest})"