from django.db import models
from django.utils.translation import gettext_lazy as _

from django.contrib.auth import get_user_model

User = get_user_model()

class Currency(models.Model):
    currency = models.CharField(verbose_name=_("currency"), max_length=4)

    def __str__(self):
        return self.currency

class Settlement(models.Model):
    
    player = models.ForeignKey(User, on_delete=models.CASCADE, default=1) # change cascade
    date = models.DateField()
    transactionUSD = models.DecimalField(
        verbose_name=_("Transaction in USD"),
        max_digits=14,
        decimal_places=2, 
        null=False, 
        blank=False, 
        default=0.00,
        help_text = "transaction in USD"
        )
    transactionValue = models.DecimalField(
        verbose_name=_("Transaction Value"),
        max_digits=14, 
        decimal_places=2, 
        null=True, 
        blank=True, 
        default=0.00,
        help_text = "OPTIONAL transaction value in other currency than USD("
        )
    currency = models.ForeignKey(
        Currency, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True,
        help_text = "OPTIONAL"
        )
    exchangeRate = models.DecimalField(
        verbose_name=_("Exchange Rate"),
        max_digits=14, 
        decimal_places=6, 
        null=True, 
        blank=True, 
        help_text = "OPTIONAL exchange rate to the USD")
    description = models.CharField(
        verbose_name=_("Description of transaction"), 
        max_length=1000, 
        blank=True, 
        null=True,
        help_text = "OPTIONAL additional info about transaction")

