from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, reverse, redirect
from django.views import View

from .forms import UserProfileForm, EmploymentForm, GuarantorForm


# Create your views here.

class IndexView(View):

    def get(self, request):
        user = request.user
        if user.is_authenticated:
            if user.profile.application_confirmed:
                return redirect(reverse("core:application_details"))
            else:
                return redirect(reverse("core:application"))
        else:
            return render(request, "pages/home.html")


class ApplicationView(LoginRequiredMixin, UserPassesTestMixin, View):
    def handle_no_permission(self):
        return redirect(reverse('core:application_details'))

    def test_func(self):
        return not self.request.user.profile.application_confirmed

    def get(self, request):
        user = request.user
        user_profile_form = UserProfileForm(initial={'user': user})
        employment_form = EmploymentForm(initial={'profile': user.profile})
        guarantor_form = GuarantorForm(initial={'profile': user.profile})

        ctx = {
            'user_profile_form': user_profile_form,
            'employment_form': employment_form,
            'guarantor_form': guarantor_form
        }

        return render(request, "pages/application.html", ctx)

    def post(self, request):
        profile = request.user.profile
        user_profile_form = UserProfileForm(request.POST, instance=profile)
        employment_form = EmploymentForm(request.POST)
        guarantor_form = GuarantorForm(request.POST)

        if user_profile_form.is_valid() and employment_form.is_valid() and guarantor_form.is_valid():
            user_profile_form.save()
            user_profile_form.save()
            guarantor_form.save()
            employment_form.save()
            profile.application_confirmed = True
            profile.save()

        return redirect(reverse("core:index"))


class ApplicationDetailsView(LoginRequiredMixin, UserPassesTestMixin, View):
    def handle_no_permission(self):
        return redirect(reverse('core:application'))

    def test_func(self):
        return self.request.user.profile.application_confirmed

    def get(self, request):
        profile = request.user.profile
        ctx = {
            'profile': profile,
        }

        return render(request, "pages/application_details.html", ctx)
