from rest_framework import serializers

from .models import Wallet


class UserWalletSerializer(serializers.ModelSerializer):
    """Сериализатор кошелька пользователя."""

    class Meta:
        model = Wallet
        fields = ('wallet_uuid', 'amount')


class OperationSerializer(serializers.Serializer):
    """Сериализатор изменения суммы в кошельке."""

    operationType = serializers.ChoiceField(choices=['DEPOSIT', 'WITHDRAW'])
    amount = serializers.IntegerField()
