from django.urls import path

from friends.views import FriendsListView, subscribe, unsubscribe

urlpatterns = [
    path('friends/', FriendsListView.as_view(), name='friends_list'),
    path('subscribe/<int:pk>', subscribe, name='subscribe'),
    path('unsubscribe/<int:pk>', unsubscribe, name='unsubscribe'),
]
