from django.views.generic.detail import DetailView

from accounts.models import User

class UserDetailView(DetailView):
    model = User
    template_name = 'accounts/users/update.html'
    login_url = '/accounts/list/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['now'] = timezone.now()
        return context