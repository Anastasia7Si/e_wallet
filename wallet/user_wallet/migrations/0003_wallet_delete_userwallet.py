# Generated by Django 5.1.6 on 2025-03-02 09:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_wallet', '0002_remove_userwallet_wallet_uuid_userwallet_wallet_uuid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('wallet_uuid', models.UUIDField(db_index=True, primary_key=True, serialize=False, verbose_name='UUID кошелька')),
                ('amount', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1, message='Минимальный размер 1!')], verbose_name='Баланс')),
            ],
        ),
        migrations.DeleteModel(
            name='UserWallet',
        ),
    ]
