from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),            # /
    path('dashboard/', views.dashboard, name='dashboard'),
    path('scan/', views.scan, name='scan'),
    path('accounts/', include('allauth.urls')),
    path('tickets/', views.tickets, name='tickets'),
    path("tickets/path_data/", views.path_data, name="path_data"),
]