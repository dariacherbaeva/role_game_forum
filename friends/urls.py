from django.urls import path, re_path

from friends.views import FriendsListView, subscribe, unsubscribe

urlpatterns = [
    path('friends/', FriendsListView.as_view(), name='friends_list'),
    re_path('subscribe/(?P<pk>\d+)', subscribe, name='subscribe'),
    path('unsubscribe/<int:pk>', unsubscribe, name='unsubscribe'),
]
