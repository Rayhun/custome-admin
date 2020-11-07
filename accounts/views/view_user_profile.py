from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views import View
from accounts.models import Profile
from .forms import ProfileForm
class ProfileView(LoginRequiredMixin,DetailView):

    model = Profile
    template_name = 'accounts/users/user_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def test_func(self):
        return self.request.user.is_active and self.request.user.is_staff


# class ProfileView(LoginRequiredMixin, View):

#     def get(self, request, *args, **kwargs):
#         profile = ProfileForm(instance=Profile.objects.filter()).first()

#         return render(request, 'accounts/users/user_profile.html',{'profile':profile})