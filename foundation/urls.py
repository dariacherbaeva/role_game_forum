from django.urls import path, re_path
from foundation.views import MainPageView as Main, registration_view as registration, ProfileView, ProfileEditView, \
    PlotView, NavigationView, RulesView, SearchResultView

urlpatterns = [
    path('register/', registration, name='registration'),
    path('', Main.as_view(), name='main_page'),
    re_path('profile/(<pk>[0-9])+/', ProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/edit', ProfileEditView.as_view(), name='profile_edit'),
    path('plot/', PlotView.as_view(), name='plot'),
    path('navigation/', NavigationView.as_view(), name='navigation'),
    path('rules/', RulesView.as_view(), name='rules'),
    path('search/', SearchResultView.as_view(), name='search'),
]
