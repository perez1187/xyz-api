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


''' 
zaladowac dane, tak aby pracowac na orginalnych danych, w tym zaladowac userow

stworzyc prosty front dla usera
stworzyc prosty front dla admina

opublikowac backend
opublikowac front

stworzyc nowy branch i nowa testowa baze

'''