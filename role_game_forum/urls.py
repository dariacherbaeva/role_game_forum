"""role_game_forum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include, re_path

from role_game_forum import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    url('', include('foundation.urls')),
    re_path(r'^characters/', include(('characters.urls', 'characters'), namespace='Characters')),
    re_path(r'^forum/', include(('forum.urls', 'forum'), namespace='Forum')),
    re_path(r'^friends/', include(('friends.urls', 'friends'), namespace='Friends')),
    re_path(r'^chat/', include(('chat.urls', 'chat'), namespace='Chat')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
