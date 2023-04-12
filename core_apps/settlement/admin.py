from django.contrib import admin

from . import models

class SettlementAdmin(admin.ModelAdmin):
    list_display = [
        "player",
        # "date", 
        "transactionUSD",
        "transactionValue",
        "currency",
        "exchangeRate",
        "description"
        ]
    list_display_links = ["player"]
    list_filter = ["player"]

admin.site.register(models.Settlement, SettlementAdmin)

class CurrencyAdmin(admin.ModelAdmin):
    list_display = [
        'currency',
    ]
    list_display_links = ['currency']

admin.site.register(models.Currency, CurrencyAdmin)    