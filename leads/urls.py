from django.urls import path
from django.http import JsonResponse
from .views import LeadCreateView

# temporary test route so /api/ works immediately
def api_home(request):
    return JsonResponse({"api": "ok"})

urlpatterns = [
    path("", api_home),
    path("leads/", LeadCreateView.as_view(), name="lead-create"),
]