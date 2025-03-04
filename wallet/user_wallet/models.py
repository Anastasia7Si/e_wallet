from django.db import models
from django.core.validators import MinValueValidator


class Wallet(models.Model):
    """Модель кошелька пользователя."""

    wallet_uuid = models.UUIDField(
        primary_key=True,
        db_index=True,
        verbose_name='UUID кошелька'
    )
    amount = models.PositiveIntegerField(
        validators=(
            MinValueValidator(0,
                              message='Минимальный размер 0!'),
        ),
        verbose_name='Баланс',
        default=0
    )

    def __str__(self):
        return str(self.wallet_uuid)
