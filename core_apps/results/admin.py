from django.contrib import admin

from . import models


class ResultsAdmin(admin.ModelAdmin):

    list_display = [
        "pk",
        "nickname", 
        "club", 
        "reportId",
        "profit_loss",
        "rake","deal",
        "rakeback",
        "adjustment",
        "agents",
        "created_at",
        "updated_at",
        "description"
        ]
    list_display_links = ["pk"]
    list_filter = ["reportId","nickname"]


admin.site.register(models.Result, ResultsAdmin)

class NicknameAdmin(admin.ModelAdmin):
    list_display = ["pk","player", "nickname","club","player_rb","player_adjustment"]
    list_display_links = ["nickname"]
    list_filter = ["player", "club","nickname"]


admin.site.register(models.Nickname, NicknameAdmin)

class ClubAdmin(admin.ModelAdmin):
    list_display = ["club","affAgent","player_rb","player_adjustment","is_active"]
    list_display_links = ["club"]
    list_filter = ["club"]


admin.site.register(models.Club, ClubAdmin)

class ReportIdAdmin(admin.ModelAdmin):
    list_display = ["pk","date","description","created_at","updated_at"] # "created_at", "updated_at"
    list_display_links = ["pk"]
admin.site.register(models.ReportId,ReportIdAdmin)

class AffAgentAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_display_links = ["name"]
admin.site.register(models.AffAgent,AffAgentAdmin)