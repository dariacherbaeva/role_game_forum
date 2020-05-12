from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView
from rest_framework_swagger.views import get_swagger_view

from forum.views import ForumListView, ForumPageView, AllSectionsView, SystemPostFormView, like, dislike, \
    GamePostFormView, PostDeleteView, SingleSectionView

schema_view = get_swagger_view(title='Sections API Documentation')

urlpatterns = [
    # app urls
    path('list/', ForumListView.as_view(), name='list'),
    path('page/<int:pk>', ForumPageView.as_view(), name='page'),
    path('new/system/', SystemPostFormView.as_view(), name='new_system'),
    path('like/<int:pk>', like, name='like'),
    path('dislike/<int:pk>', dislike, name='dislike'),
    path('new/game/', GamePostFormView.as_view(), name='new_game'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='delete'),

    # api urls
    path('api/sections/', AllSectionsView.as_view(), name='api_sections'),
    path('api/sections/<int:pk>/', SingleSectionView.as_view(), name='api_section'),
    url(r'^documentation/', schema_view, name='doc'),
]
