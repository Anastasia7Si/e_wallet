from django.contrib import admin

from .models import Wallet


class UserWalletAdmin(admin.ModelAdmin):
    list_display = ('wallet_uuid', 'amount')
    list_filter = ('wallet_uuid',)
    empty_value_display = '-пусто-'


admin.site.register(Wallet)
