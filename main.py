from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager

api_key = 'pRhox5rpZNKcQSDIzT0NzYk3sfe5OmrZinkOGnhfAzlZ759WNUpe6o4tavfZXJnN'
api_secret = 'pRhox5rpZNKcQSDIzT0NzYk3sfe5OmrZinkOGnhfAzlZ759WNUpe6o4tavfZXJnN'


client = Client(api_key, api_secret)

#Just change it with the pair of our trade
paire = 'VETUSDT'

depth = client.get_order_book(symbol=paire)
price = depth['bids'][0][0]


def bot(enterPrice, stopLoss, maxLoss):
    res = enterPrice - stopLoss

    bet = (maxLoss / res) * price
    print('rgudrg')
    print(bet)

