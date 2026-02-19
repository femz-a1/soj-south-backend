from django.urls import path
from django.http import JsonResponse

# temporary test route so /api/ works immediately
def api_home(request):
    return JsonResponse({"api": "ok"})

urlpatterns = [
    path("", api_home),
]