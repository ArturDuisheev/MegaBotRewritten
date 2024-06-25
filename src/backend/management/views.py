import subprocess

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import User


@csrf_exempt
def get_user(request):
    if request.method == 'POST':
        get_username = subprocess.run(["powershell", "-File", "Scripts/get_user.ps1"])
        User.objects.create(username=get_username)
        return JsonResponse({"status": 'success', 'data': request.data})


def block_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        user = User.objects.get(username=username)
        if user:
            user.is_blocked = True
            user.save()
            subprocess.run(["powershell", "-File", "Scripts/block_user.ps1",
                            "-username", username],
                           capture_output=True, text=True)
            return JsonResponse({"status": "success", "message": f"User {username} blocked."})
        return JsonResponse({"status": "error", "message": "User not found."})
    return JsonResponse({"status": "error", "message": "Invalid request method."})


