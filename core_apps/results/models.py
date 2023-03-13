from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()

class Club(models.Model):
    club = models.CharField(verbose_name=_("Club"), max_length=100, unique=False)
    player_rb = models.DecimalField(verbose_name=_("Player Rakeback"),max_digits=10, decimal_places=3, null=False, blank=False, default=0.0)
    player_adjustment = models.DecimalField(verbose_name=_("Player Adjustment"),max_digits=10, decimal_places=2, null=False, blank=False, default=0.0)
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

    nickname = models.OneToOneField(Nickname, related_name="nicknameOne", on_delete=models.CASCADE,default=1)
    # player = models.ForeignKey(Nickname,on_delete=models.CASCADE, verbose_name=_("Player"), related_name="Result_Player_Nickname", blank=True, null=True)
    # nickname = models.ForeignKey(Nickname,on_delete=models.CASCADE, verbose_name=_("Nickname"), related_name="Result_Nickname_Nickname", blank=True, null=True)
    # club = models.ForeignKey(Nickname,on_delete=models.CASCADE, verbose_name=_("Club"), related_name="Result_Club_Nickname", blank=True, null=True)
  
  