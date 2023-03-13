from django.contrib import admin

from . import models


class ResultsAdmin(admin.ModelAdmin):
    # list_display = ["club","player", "nickname"]
    # list_display_links = ["club","player", "nickname"]
    # list_filter = ["player", "nickname"]
    list_display = ["nickname"]
    list_display_links = ["nickname"]
    list_filter = [ "nickname"]


admin.site.register(models.Result, ResultsAdmin)

class NicknameAdmin(admin.ModelAdmin):
    list_display = ["club","player", "nickname"]
    list_display_links = ["club","player", "nickname"]
    list_filter = ["player", "nickname"]


admin.site.register(models.Nickname, NicknameAdmin)

class ClubAdmin(admin.ModelAdmin):
    list_display = ["club","player_rb","player_adjustment","is_active"]
    list_display_links = ["club"]
    list_filter = ["club"]


admin.site.register(models.Club, ClubAdmin)