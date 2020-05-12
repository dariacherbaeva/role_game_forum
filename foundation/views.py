from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, UpdateView, ListView

from forum.models import Post
from foundation.forms import SiteRegistrationForm
from foundation.models import SiteUser
from friends.models import Subscription


def registration_view(request):
    context = {}
    if request.POST:
        form = SiteRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            # account = authenticate(email=email, password=raw_password)
            # login(request, account)
            return redirect('login')
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts_counter'] = Post.objects.filter(author_id=self.object.id).count()
        if self.object != self.request.user:
            if Subscription.objects.filter(subscriber_id=self.request.user.id, subscriptor_id=self.object.id).exists():
                context['is_sub'] = True
            else:
                context['is_sub'] = False
        return context


class ProfileEditView(UpdateView):
    template_name = 'foundation/profile_edit.html'
    model = SiteUser
    fields = ('email', 'username', 'status', 'photo')
    success_url = reverse_lazy('main_page')


class PlotView(TemplateView):
    template_name = 'foundation/plot.html'


class NavigationView(TemplateView):
    template_name = 'foundation/navigation.html'


class RulesView(TemplateView):
    template_name = 'foundation/rules.html'


class SearchResultView(ListView):
    model = SiteUser
    template_name = 'foundation/search_result.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = SiteUser.objects.filter(
            Q(username__icontains=query) | Q(email__icontains=query)
        )
        return object_list
