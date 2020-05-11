from django.contrib import admin

from forum.models import Section, Theme, Post, Like, Dislike


class SectionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


class ThemeAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ('section',)


class PostAdmin(admin.ModelAdmin):
    search_fields = ('text',)
    list_filter = ('theme', 'author',)


class LikeAdmin(admin.ModelAdmin):
    list_filter = ('user', 'post',)


class DislikeAdmin(admin.ModelAdmin):
    list_filter = ('user', 'post',)


admin.site.register(Section, SectionAdmin)
admin.site.register(Theme, ThemeAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(Dislike, DislikeAdmin)
