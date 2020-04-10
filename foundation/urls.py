from django.urls import path
from foundation.views import MainPageView as Main, registration_view as registration, ProfileView, ProfileEditView, \
    PlotView, NavigationView, SubjectsListView, RulesView

urlpatterns = [
    path('register/', registration, name='registration'),
    path('', Main.as_view(), name='main_page'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/edit', ProfileEditView.as_view(), name='profile_edit'),
    path('plot/', PlotView.as_view(), name='plot'),
    path('navigation/', NavigationView.as_view(), name='navigation'),
    path('school/', SubjectsListView.as_view(), name='school'),
    path('rules/', RulesView.as_view(), name='rules')
]
