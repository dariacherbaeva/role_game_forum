from django.contrib import admin

from chat.models import Message


class MessageAdmin(admin.ModelAdmin):
    search_fields = ('text',)
    list_filter = ('from_who', 'to_who', 'when',)


admin.site.register(Message, MessageAdmin)
