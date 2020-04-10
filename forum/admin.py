from django.contrib import admin

from forum.models import Section, Theme, Post, Like, Dislike

admin.site.register(Section)
admin.site.register(Theme)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Dislike)
