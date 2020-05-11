from django.conf.urls import url
from django.urls import path
from rest_framework_swagger.views import get_swagger_view

from forum.views import ForumListView, ForumPageView, AllSectionsView, SystemPostFormView, like, dislike, \
    GamePostFormView, PostDeleteView, SingleSectionView

urlpatterns = [
    path('list/', ForumListView.as_view(), name='list'),
    path('page/<int:pk>', ForumPageView.as_view(), name='page'),
    path('api/sections/', AllSectionsView.as_view(), name='sections'),
    path('api/sections/<int:pk>/', SingleSectionView.as_view(), name='section'),
    path('new/system/', SystemPostFormView.as_view(), name='new_system'),
    path('like/<int:pk>', like, name='like'),
    path('dislike/<int:pk>', dislike, name='dislike'),
    path('new/game/', GamePostFormView.as_view(), name='new_game'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='delete'),
]
