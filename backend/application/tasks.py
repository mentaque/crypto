import requests
from celery import shared_task

from application.models import Cryptocurrency


@shared_task
def get_crypto():

    api_key = '8bc6be42-2e3a-4465-84bb-af2c8ae769a4'

    parameters = {
        'start': '1',
        'convert': 'USD',
    }

    url = f'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY={api_key}'
    response = requests.get(url, params=parameters)

    if response.status_code == 200:
        data = response.json()
        for coin in data['data']:
            name = coin['name']
            symbol = coin['symbol']
            price = round(coin['quote']['USD']['price'], 4)
            volume = round(coin['quote']['USD']['volume_24h'], 4)
            percent_change_1h = round(coin['quote']['USD']['percent_change_1h'], 4)
            percent_change_24h = round(coin['quote']['USD']['percent_change_24h'], 4)
            percent_change_7d = round(coin['quote']['USD']['percent_change_7d'], 4)
            percent_change_30d = round(coin['quote']['USD']['percent_change_30d'], 4)

            try:
                cryptocurrency = Cryptocurrency.objects.get(symbol=symbol)
                cryptocurrency.name = name
                cryptocurrency.price = price
                cryptocurrency.volume_24h = volume
                cryptocurrency.percent_change_1h = percent_change_1h
                cryptocurrency.percent_change_24h = percent_change_24h
                cryptocurrency.percent_change_7d = percent_change_7d
                cryptocurrency.percent_change_30d = percent_change_30d
                cryptocurrency.save()
            except Cryptocurrency.DoesNotExist:
                Cryptocurrency.objects.create(
                    name=name,
                    symbol=symbol,
                    price=price,
                    volume_24h=volume,
                    percent_change_1h=percent_change_1h,
                    percent_change_24h=percent_change_24h,
                    percent_change_7d=percent_change_7d,
                    percent_change_30d=percent_change_30d
                )

    else:
        print('Ошибка при запросе данных')