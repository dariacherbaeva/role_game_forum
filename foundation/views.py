from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView, DetailView, UpdateView

from foundation.forms import SiteRegistrationForm
from foundation.models import SiteUser


def registration_view(request):
    context = {}
    if request.POST:
        form = SiteRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('main_page')
        else:
            context['registration_form'] = form
    else:
        form = SiteRegistrationForm()
        context['registration_form'] = form
    return render(request, 'registration/register.html', context)


class MainPageView(TemplateView):
    template_name = 'foundation/main_page.html'


class ProfileView(DetailView):
    model = SiteUser
    template_name = 'foundation/profile.html'


class ProfileEditView(UpdateView):
    template_name = 'foundation/profile_edit.html'
    model = SiteUser
    fields = ('email', 'username', 'status', 'photo')
    success_url = 'profile'


class PlotView(TemplateView):
    template_name = 'foundation/plot.html'


class NavigationView(TemplateView):
    template_name = 'foundation/navigation.html'


class RulesView(TemplateView):
    template_name = 'foundation/rules.html'
