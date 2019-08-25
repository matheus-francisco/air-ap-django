from django.contrib import admin

from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_diplay = ('id', 'name', 'listing', 'email', 'contact_date')
    list_diplay_links = ('id', 'name')
    search_fields = ('name', 'email', 'listing')
    list_per_page = 25


admin.site.register(Contact, ContactAdmin)

