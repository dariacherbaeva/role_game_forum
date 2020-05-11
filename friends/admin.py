from django.contrib import admin

from friends.models import Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    list_filter = ('subscriptor', 'subscriber',)


admin.site.register(Subscription, SubscriptionAdmin)
