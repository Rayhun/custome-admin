from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views import View
from accounts.models import Profile
from .forms import ProfileForm
from django.contrib.auth import get_user_model
User = get_user_model()
# class ProfileView(LoginRequiredMixin,DetailView):

#     model = Profile
#     template_name = 'accounts/users/user_profile.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context

#     def test_func(self):
#         return self.request.user.is_active and self.request.user.is_staff


class ProfileView(LoginRequiredMixin, UserPassesTestMixin, View):
    

    def get(self, request, *args, **kwargs):
        profile_id = request.user.id
        profile = ProfileForm(instance=Profile.objects.filter(pk=profile_id).first())
        contex = {
            'profile_id':profile_id,
            'profile':profile
        }
        return render(request, 'accounts/users/user_profile.html',contex)

    def test_func(self):
        return self.request.user.is_active and self.request.user.is_staff


class ProfileupdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    template_name = 'accounts/users/user_profile_update.html/'
    model = User
    fields = ['name', 'date_of_birth']
    success_url = 'accounts/users/profile/'

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = self.get_object()
        self.profile_object = Profile.objects.filter(user=self.object).first()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        profile_form = ProfileForm(instance=self.profile_object)
        return self.render_to_response(
            self.get_context_data(form=form,profile_form=profile_form))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = self.get_object()
        self.profile_object = Profile.objects.filter(user=self.object).first()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        profile_form = ProfileForm(self.request.POST, instance=self.profile_object)
        if (form.is_valid() and profile_form.is_valid()):
            return self.form_valid(form, profile_form)
        else:
            return self.form_invalid(form, profile_form)

    def form_valid(self, form, profile_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()

        profile_form.user = self.object
        profile_form.save()

        return HttpResponseRedirect(reverse_lazy('accounts_users_profile'))

    def form_invalid(self, form, profile_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                                  profile_form=profile_form))


    def test_func(self):
        return self.request.user.is_active and self.request.user.is_staff





















# class ProfileupdateView(LoginRequiredMixin,UserPassesTestMixin,View):

#     def get(self, request, *args, **kwargs):
#         profile_id = request.user.id
#         profile = ProfileForm(instance=Profile.objects.filter(pk=profile_id).first())
#         return render(request, 'accounts/users/user_profile_update.html',{'profile':profile})


#     def post(self, request, *args, **kwargs):
#         profile_id = request.user.id
#         obj = Profile.objects.filter(pk=profile_id).first()
#         profile = ProfileForm(self.request.POST, self.request.FILES, instance=obj)
#         if profile.is_valid():
#             profile.save()
#             return redirect('accounts_users_profile')
#         else:
#             return render(request, 'accounts/users/user_profile_update.html',{'profile':profile})

#     def test_func(self):
#         return self.request.user.is_active and self.request.user.is_staff
