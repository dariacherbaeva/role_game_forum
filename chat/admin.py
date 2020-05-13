from django.contrib import admin

from chat.models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('from_who', 'to_who', 'text',)
    search_fields = ('text',)
    list_filter = ('from_who', 'to_who', 'when',)


admin.site.register(Message, MessageAdmin)
