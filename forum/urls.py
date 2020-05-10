from django.urls import path

from forum.views import ForumListView, ForumPageView, AllSectionView, SystemPostFormView, like, dislike

urlpatterns = [
    path('list/', ForumListView.as_view(), name='list'),
    path('page/<int:pk>', ForumPageView.as_view(), name='page'),
    path('api/sections/', AllSectionView.as_view(), name='sections'),
    path('new/system/', SystemPostFormView.as_view(), name='new_system'),
    path('like/<int:pk>', like, name='like'),
    path('dislike/<int:pk>', dislike, name='dislike')
]
