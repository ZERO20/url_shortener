from django.contrib import admin
from apps.url_management.models import Shortener
# Register your models here.


@admin.register(Shortener)
class ShortenerAdmin(admin.ModelAdmin):
    fields = ('url', 'shortcode', 'created_at', 'updated_at',)
    readonly_fields = ('created_at', 'updated_at',)
    list_display = ('url', 'shortcode', 'created_at',)
    list_filter = ('created_at',)
    search_fields = ('url', 'short_code')
