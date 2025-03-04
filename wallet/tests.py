import os
import django
import pytest
from django.urls import reverse
from rest_framework import status


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wallet.settings')
django.setup()

from rest_framework.test import APIClient
from user_wallet.models import Wallet


@pytest.mark.django_db
class TestWalletViews:
    """Сет тестов для кошелька пользователя."""

    def setup_method(self):
        self.client = APIClient()
        self.wallet = Wallet.objects.create(
            wallet_uuid="123e4567-e89b-12d3-a456-426614174000",
            amount=100
            )

    def test_wallet_operation_deposit(self):
        url = reverse('wallet_operation',
                      kwargs={'wallet_uuid': self.wallet.wallet_uuid})
        response = self.client.post(
            url, {'operationType': 'DEPOSIT', 'amount': 50},
            format='json')

        assert response.status_code == status.HTTP_200_OK
        assert response.data['balance'] == '150'

    def test_wallet_operation_withdraw(self):
        url = reverse('wallet_operation',
                      kwargs={'wallet_uuid': self.wallet.wallet_uuid})
        response = self.client.post(
            url, {'operationType': 'WITHDRAW', 'amount': 30},
            format='json')

        assert response.status_code == status.HTTP_200_OK
        assert response.data['balance'] == '70'

    def test_wallet_operation_withdraw_insufficient_funds(self):
        url = reverse('wallet_operation',
                      kwargs={'wallet_uuid': self.wallet.wallet_uuid})
        response = self.client.post(
            url, {'operationType': 'WITHDRAW', 'amount': 200},
            format='json')

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['error'] == 'Insufficient funds'

    def test_wallet_operation_wallet_not_found(self):
        url = reverse(
            'wallet_operation',
            kwargs={'wallet_uuid': '2d385639-da3b-4f90-b8bb-724c1eb64601'})
        response = self.client.post(
            url, {'operationType': 'DEPOSIT', 'amount': 50},
            format='json')

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.data['error'] == 'Wallet not found'

    def test_wallet_operation_invalid_data(self):
        url = reverse('wallet_operation',
                      kwargs={'wallet_uuid': self.wallet.wallet_uuid})
        response = self.client.post(
            url, {'operationType': 'DEPOSIT'},
            format='json')

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert 'error' in response.data

    def test_get_wallet_balance(self):
        url = reverse('get_wallet_balance',
                      kwargs={'wallet_uuid': self.wallet.wallet_uuid})
        response = self.client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data['amount'] == 100

    def test_get_wallet_balance_not_found(self):
        url = reverse(
            'get_wallet_balance',
            kwargs={'wallet_uuid': '2d385639-da3b-4f90-b8bb-724c1eb64601'})
        response = self.client.get(url)

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.data['error'] == 'Wallet not found'
