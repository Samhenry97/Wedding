from django.contrib import admin

from django.contrib import admin
from .models import RSVP


admin.site.site_header = 'Samari Admin'
admin.site.site_title = 'Samari Admin'


# Register models to admin pages
def message_exists(obj):
    exists = obj.message and obj.message.strip()
    return u'\u2713' if exists else ''
message_exists.short_description = 'Message'


class RSVPAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'number', 'attending', message_exists, 'created')


admin.site.register(RSVP, RSVPAdmin)
