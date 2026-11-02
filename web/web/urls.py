from django.urls import path
import dashboard_api

urlpatterns = [
    path("", dashboard_api.dashboard_home, name="dashboard_home"),
    path("api/processes/", dashboard_api.api_processes, name="api_processes"),
    path("api/manage_process/", dashboard_api.api_manage_process, name="api_manage_process"),
]
