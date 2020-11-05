from django.contrib.auth import views as auth_views
from django.urls import path

from accounts.views.auth_login.dashboard_view import DashboardView
from accounts.views.view_users import UserListView                          
urlpatterns = [
    path('login/',auth_views.LoginView.as_view(),name='accounts_login'),
    path('logout/', auth_views.LogoutView.as_view(), name='accounts_logout'),
    path('dashboard/', DashboardView.as_view(), name='accounts_dashboard'),

    # user urls
    path('users/list/',UserListView.as_view(), name='accounts_users_list'),
]