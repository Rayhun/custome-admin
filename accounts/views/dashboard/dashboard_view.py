from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.list import ListView
from accounts.models import User

class DashboardView(LoginRequiredMixin,UserPassesTestMixin, TemplateView):

    template_name = 'accounts/dashboard.html'
    login_url = '/accounts/login/'
    paginate_by = 5


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['total_user'] = User.objects.all().order_by('-pk')[:3]
        context['total_regis'] = User.objects.all().count()
        context['total_admin'] = User.objects.filter(is_admin=True).count()
        context['total_customer'] = User.objects.filter(is_admin=False).count()
        return context
    
    def test_func(self):
        return self.request.user.is_active and self.request.user.is_staff
