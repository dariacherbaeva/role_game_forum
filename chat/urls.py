from django.urls import path

from chat.views import NewMessageView, MyMessagesListView

urlpatterns = [
    path('new/', NewMessageView.as_view(), name='new'),
    path('messages/', MyMessagesListView.as_view(), name='messages')
]
