from django.urls import path

from dashboard.views import admin_dashboard

urlpatterns = [
    path('admin-dashboard', admin_dashboard, name='admin-dashboard'),
]