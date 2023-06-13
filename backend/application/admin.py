from django.contrib import admin

from application.models import Cryptocurrency


class CryptocurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol', 'price', 'volume_24h', 'percent_change_1h', 'percent_change_24h', 'percent_change_7d', 'percent_change_30d', 'last_update')

admin.site.register(Cryptocurrency, CryptocurrencyAdmin)
