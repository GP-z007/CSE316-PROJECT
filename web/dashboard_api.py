import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

LXD_AGENT_URL = "http://10.10.10.10:8000"

def dashboard_home(request):
    # Agent 163eed4: Builds the KasmVNC URL from the host in the current request.
    host = request.get_host().split(":")[0]
    kasm_url = f"http://{host}:8444/vnc.html?autoconnect=true&resize=scale&reconnect=true"
    return render(request, "process_dashboard.html", {"kasm_url": kasm_url})

def api_processes(request):
    try:
        r = requests.get(f"{LXD_AGENT_URL}/processes", timeout=2)
        return JsonResponse(r.json(), safe=False)
    except Exception as e:
        return JsonResponse({"error": True, "message": str(e)}, status=502)

@csrf_exempt
def api_manage_process(request):
    if request.method != "POST":
        return JsonResponse({"error": True, "message": "POST required"}, status=405)
    pid = request.POST.get("pid")
    action = request.POST.get("action", "kill")
    try:
        r = requests.post(f"{LXD_AGENT_URL}/manage_process", data={"pid": pid, "action": action}, timeout=2)
        return JsonResponse(r.json(), safe=False)
    except Exception as e:
        return JsonResponse({"error": True, "message": str(e)}, status=502)
