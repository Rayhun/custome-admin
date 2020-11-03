from django.contrib.auth import views as auth_views
from django.urls import path

from accounts.views.auth_login.dashboard_view import DashboardView

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(),name='accounts_login'),
    path('logout/', auth_views.LogoutView.as_view(), name='accounts_logout'),
    path('dashboard/', DashboardView.as_view(), name='accounts_dashboard'),
]