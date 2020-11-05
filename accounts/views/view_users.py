from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from accounts.models import User

class UserListView(LoginRequiredMixin,UserPassesTestMixin, ListView):

    template_name = 'accounts/users/list.html'
    login_url = '/accounts/login/'
    model = User
    paginate_by = 1
    # permission_required = "view_user"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def test_func(self):
        return self.request.user.is_active and self.request.user.is_staff
