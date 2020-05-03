from django.urls import path

from forum.views import ForumListView, ForumPageView

urlpatterns = [
    path('list/', ForumListView.as_view(), name='list'),
    path('page/<int:pk>', ForumPageView.as_view(), name='page'),
]
