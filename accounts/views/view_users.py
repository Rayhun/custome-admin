from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView,CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

from accounts.models import User,Profile

from accounts.filters import UserFilter

class UserListView(LoginRequiredMixin,UserPassesTestMixin, ListView):
    template_name = 'accounts/users/list.html'
    login_url = '/accounts/login/'
    model = User


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['UserFilter'] = UserFilter(self.request.GET)
        return context

    def get_queryset(self):
        qs = User.objects.all()
        filtered_users = UserFilter(self.request.GET, queryset=qs)
        return filtered_users.qs
   
    def test_func(self):
        return self.request.user.is_active and self.request.user.is_staff


class UserCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = User
    fields = ['name','email','date_of_birth']
    template_name = "accounts/users/create.html"
    success_url = reverse_lazy('accounts_users_list')

    def test_func(self):
        return self.request.user.is_active and self.request.user.is_staff


class UserUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = User
    fields = ['name','email','date_of_birth']
    success_url = "/accounts/users/list/"
    template_name = "accounts/users/update.html"

    def test_func(self):
        return self.request.user.is_active and self.request.user.is_staff


class UserDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = User
    success_url = reverse_lazy('accounts_users_list')

    def test_func(self):
        return self.request.user.is_active and self.request.user.is_staff











