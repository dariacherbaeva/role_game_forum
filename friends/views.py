from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView

from foundation.models import SiteUser
from friends.models import Subscription


class FriendsListView(TemplateView):
    template_name = 'friends/friends_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subscribers_s = Subscription.objects.filter(subscriptor_id=self.request.user.id)
        subscribers = []
        for sub in subscribers_s:
            subscribers.append(sub.subscriber)
        subscriptions_s = Subscription.objects.filter(subscriber_id=self.request.user.id)
        subscriptions = []
        for sub in subscriptions_s:
            subscriptions.append(sub.subscriptor)
        friends = []
        for u in SiteUser.objects.exclude(id=self.request.user.id):
            if subscriptions_s.filter(subscriptor_id=u.id).exists() & subscribers_s.filter(subscriber_id=u.id).exists():
                friends.append(u)
        context['friends'] = friends
        context['subscribers'] = list(set(subscribers) - set(friends))
        context['subscriptions'] = list(set(subscriptions) - set(friends))
        return context


@login_required
def subscribe(request, pk):
    Subscription.objects.create(subscriber=request.user, subscriptor_id=pk)
    next_page = request.POST.get('next', '/')
    return HttpResponseRedirect(next_page)


@login_required
def unsubscribe(request, pk):
    Subscription.objects.get(subscriber=request.user, subscriptor_id=pk).delete()
    next_page = request.POST.get('next', '/')
    return HttpResponseRedirect(next_page)


