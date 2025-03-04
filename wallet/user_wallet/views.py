from django.db import transaction
from django.db import DatabaseError
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Wallet
from .serializers import UserWalletSerializer, OperationSerializer


@api_view(['POST'])
def wallet_operation(request, wallet_uuid):
    """Вью для операций с кошельком."""

    try:
        with transaction.atomic():
            wallet = Wallet.objects.select_for_update().get(
                wallet_uuid=wallet_uuid
                )
    except Wallet.DoesNotExist:
        return Response(
            {'error': 'Wallet not found'},
            status=status.HTTP_404_NOT_FOUND
            )
    serializer = OperationSerializer(data=request.data)
    if serializer.is_valid():
        operation_type = serializer.validated_data['operationType']
        amount = serializer.validated_data['amount']
        try:
            with transaction.atomic():
                if operation_type == 'DEPOSIT':
                    wallet.amount += amount
                elif operation_type == 'WITHDRAW':
                    if wallet.amount < amount:
                        return Response(
                            {'error': 'Insufficient funds'},
                            status=status.HTTP_400_BAD_REQUEST
                            )
                    wallet.amount -= amount
                wallet.save()
                return Response(
                    {'balance': str(wallet.amount)},
                    status=status.HTTP_200_OK
                    )
        except DatabaseError:
            return Response(
                {'error': 'Database error'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    return Response(
        {'error': 'Invalid data', 'details': serializer.errors},
        status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_wallet_balance(request, wallet_uuid):
    """Вью для просмотра кошелька."""

    try:
        wallet = Wallet.objects.get(wallet_uuid=wallet_uuid)
    except Wallet.DoesNotExist:
        return Response(
            {'error': 'Wallet not found'},
            status=status.HTTP_404_NOT_FOUND
            )
    serializer = UserWalletSerializer(wallet)
    return Response(serializer.data, status=status.HTTP_200_OK)
