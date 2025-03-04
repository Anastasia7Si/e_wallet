import os
import uuid
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wallet.settings')
django.setup()

from user_wallet.models import Wallet


def create_wallet():
    new_wallet_uuid = uuid.uuid4()
    wallet = Wallet(wallet_uuid=new_wallet_uuid, amount=100)

    wallet.save()

    print(f'Создан кошелек с UUID: {wallet.wallet_uuid}'
          f' и балансом: {wallet.amount}')


if __name__ == '__main__':
    for i in range(5):
        create_wallet()
