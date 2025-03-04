from django.urls import path

from .views import wallet_operation, get_wallet_balance

urlpatterns = [
    path('api/v1/wallets/<uuid:wallet_uuid>/operation/',
         wallet_operation,
         name='wallet_operation'),
    path('api/v1/wallets/<uuid:wallet_uuid>/',
         get_wallet_balance,
         name='get_wallet_balance'),
]
