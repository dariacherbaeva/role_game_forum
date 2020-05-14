from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, ListView

from chat.models import Message


class NewMessageView(LoginRequiredMixin, CreateView):
    model = Message
    fields = ['text', 'to_who']
    template_name = 'chat/new_message.html'
    success_url = reverse_lazy('main_page')

    def form_valid(self, form):
        form.instance.from_who = self.request.user
        form.instance.when = timezone.now()
        return super(NewMessageView, self).form_valid(form)


class MyMessagesListView(LoginRequiredMixin, ListView):
    model = Message
    template_name = 'chat/messages.html'

    def get_context_data(self, **kwargs):
        context = super(MyMessagesListView, self).get_context_data(**kwargs)
        context['my_messages'] = Message.objects.filter(from_who_id=F('id'))
        return context


