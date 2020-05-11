from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, ListView

from chat.models import Message


class NewMessageView(CreateView):
    model = Message
    fields = ['text', 'to_who']
    template_name = 'chat/new_message.html'
    success_url = reverse_lazy('main_page')

    def form_valid(self, form):
        form.instance.from_who = self.request.user
        form.instance.when = timezone.now()
        return super(NewMessageView, self).form_valid(form)


class MyMessagesListView(ListView):
    model = Message
    template_name = 'chat/messages.html'
