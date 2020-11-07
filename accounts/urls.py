from django.contrib.auth import views as auth_views
from django.urls import path

from accounts.views.dashboard.dashboard_view import DashboardView
from accounts.views.view_users import UserListView, UserCreateView, UserUpdateView, UserDeleteView
from accounts.views.view_user_profile import ProfileView


urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name="accounts/registration/login.html"),name='accounts_login'),
    path('logout/', auth_views.LogoutView.as_view(), name='accounts_logout'),
    path('dashboard/', DashboardView.as_view(), name='accounts_dashboard'),

    # user urls
    path('users/list/',UserListView.as_view(), name='accounts_users_list'),
    path('users/create/',UserCreateView.as_view(), name='accounts_users_create'),
    path('users/<int:pk>/update/',UserUpdateView.as_view(), name='accounts_users_update'),
    path('users/<int:pk>/delete/',UserDeleteView.as_view(), name='accounts_users_delete'),

    path('users/<int:pk>/profile/',ProfileView.as_view(), name='accounts_users_profile')
]