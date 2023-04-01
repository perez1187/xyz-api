from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from datetime import datetime

from pandas import DataFrame

User = get_user_model()

class ReportId(models.Model):
#     pkid = models.BigAutoField(primary_key=True, editable=False)
#     id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(verbose_name=_("Name"), max_length=100, default="")
    description = models.CharField(verbose_name=_("Description"), max_length=1024, default="", null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    date = models.DateField()

    # here add report date (week from to)
    def __str__(self):
        return f"{self.date}"[0:10]    


class Club(models.Model):
    club = models.CharField(verbose_name=_("Club"), max_length=100, unique=False)
    player_rb = models.DecimalField(verbose_name=_("Aff Rakeback"),max_digits=10, decimal_places=3, null=False, blank=False, default=0.0)
    player_adjustment = models.DecimalField(verbose_name=_("Aff Adjustment"),max_digits=10, decimal_places=2, null=False, blank=False, default=0.0)
    is_active = models.BooleanField(verbose_name=_("Is Active"), default=True)

    def __str__(self):
        return f"{self.club}"

class Nickname(models.Model):
    player = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_("user"), related_name="Nickname_Player_User", default=2   # this has to be change on production
    )
    nickname = models.CharField(verbose_name=_("Nickname"), max_length=100)
    club = models.ForeignKey(Club,on_delete=models.CASCADE, verbose_name=_("Club"), related_name="Nickname_Club_Club", blank=True, null=True)
  
    player_rb = models.DecimalField(verbose_name=_("Player Rakeback"),max_digits=10, decimal_places=3, null=False, blank=False, default=0.0)
    player_adjustment = models.DecimalField(verbose_name=_("Player Adjustment"),max_digits=10, decimal_places=2, null=False, blank=False, default=0.0)

    def __str__(self):
        # return f"{self.player.nickname}"
        return f"{self.nickname}"

    class Meta:
        unique_together = ["nickname", "club"]



class Result(models.Model):
    # player = models.ForeignKey(
    #     User, on_delete=models.CASCADE, verbose_name=_("user"), related_name="nickname3", default=2   # this has to be change on production
    # )
    nickname = models.ForeignKey(Nickname,on_delete=models.CASCADE, verbose_name=_("Nickname"), related_name="Result_Nickname_Nickname", blank=True, null=True)
    club = models.ForeignKey(Club,on_delete=models.CASCADE, verbose_name=_("Club"), related_name="Result_Club_Nickname", blank=True, null=True)
    reportId = models.ForeignKey(ReportId,on_delete=models.CASCADE, verbose_name=_("ReportId"), related_name="reportID2", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.CharField(verbose_name=_("Description"), default="", max_length=512, blank=True)   
    agents = models.CharField(verbose_name=_("Agent"), max_length=100,default="", blank=True)
    profit_loss = models.DecimalField(verbose_name=_("PROFIT/LOSS"),max_digits=15, decimal_places=2, null=False, blank=False, default=0.0)
    rake = models.DecimalField(verbose_name=_("Rake"),max_digits=15, decimal_places=2, null=False, blank=False, default=0.0)
    deal = models.DecimalField(verbose_name=_("Affiliate Deal"),max_digits=10, decimal_places=3, null=False, blank=False, default=0.0) 
    rakeback = models.DecimalField(verbose_name=_("Affiliate Rakeback"),max_digits=15, decimal_places=2, null=False, blank=False, default=0.0)
    adjustment = models.DecimalField(verbose_name=_("Affiliate Adjustment"),max_digits=15, decimal_places=2, null=False, blank=False, default=0.0)
    agent_settlement = models.DecimalField(verbose_name=_("Agent Settlement"),max_digits=15, decimal_places=2, null=False, blank=False, default=0.0)
    # date = models.DateTimeField(verbose_name=_("Date: mon-sund"),default=datetime.now) 
    # nammmm = models.CharField(max_length=10, default="")

    # nickname = models.OneToOneField(Nickname, related_name="nicknameOne", on_delete=models.CASCADE,default=1,unique=False)
    # reportId = models.OneToOneField(ReportId, related_name="reportIDn", on_delete=models.CASCADE, default=1,unique=False)
    # player = models.ForeignKey(Nickname,on_delete=models.CASCADE, verbose_name=_("Player"), related_name="Result_Player_Nickname", blank=True, null=True)
    # nickname = models.ForeignKey(Nickname,on_delete=models.CASCADE, verbose_name=_("Nickname"), related_name="Result_Nickname_Nickname", blank=True, null=True)

    # def __str__(self):
    #     return 

    # def result_dataframe(self) -> DataFrame:
    #     """
    #     Get all pricing data, as a Pandas DataFrame object, for a given Stock.
    #     Returns:
    #         Pandas DataFrame
    #     """
    #     return DataFrame.from_records(Quote.objects.filter(result=self).values())