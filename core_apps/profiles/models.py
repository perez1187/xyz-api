import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from core_apps.common.models import TimeStampedUUIDModel

User = get_user_model()


class Profile(TimeStampedUUIDModel):
    # pkid = models.BigAutoField(primary_key=True, editable=False)
    # id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)

    description = models.TextField(
        verbose_name=_("description"),
        default="...",
    )

    def __str__(self):
        return f"{self.user.username}'s profile"


