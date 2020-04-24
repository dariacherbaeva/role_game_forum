from django.urls import path

from forum.views import ForumListView

urlpatterns = [
    path('list/', ForumListView.as_view(), name='list'),
]
