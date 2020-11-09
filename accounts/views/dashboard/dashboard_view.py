from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import User

class DashboardView(LoginRequiredMixin, TemplateView):

    template_name = 'accounts/dashboard.html'
    login_url = '/accounts/login/'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_customer'] = User.objects.all().count()
        return context
