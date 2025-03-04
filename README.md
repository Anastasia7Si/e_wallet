# e_wallet
Тестовое задание для JavaCode.
Электронный кошелёк.

## Автор

- **Анастасия Пушкарная** - [GitHub](https://github.com/Anastasia7Si)

## Технологии
- Python 3.11
- Django 5.1.6
- Django REST framework 3.15.2
- Nginx
- Docker
- Postgres

## Эндпоинты API
Вот основные конечные точки API и как к ним обратиться:
- .../api/v1/wallets/<uuid:wallet_uuid>/operation/
- .../api/v1/wallets/<uuid:wallet_uuid>/

## Реализовано:
- Возможность просматривать баланс пошелька по uuid.
- Возможность пополнять и списывать средства с кошелька.
- Тесты для энедпоинтов. 
- Обработка невалидных данных.
- Запуск проекта в Docker-контейнере.

### Как запустить проект в контейнерах (доступ по http://localhost:80/api/)
- Клонировать репозиторий и перейти в него в командной строке:
```
git@github.com:Anastasia7Si/e_wallet.git
cd e_wallet
```
- При создать свой .env-файл и внести в него свои данные, чтобы настроить для работы с PostgreSQL напримере env.example.
```
- Запустить сборку  проекта:

```
docker-compose up -d
```
