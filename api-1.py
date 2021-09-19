#Importing Libraries
from binance.client import Client
import configparser
import json
import pprint
import asyncio
from binance import AsyncClient

#Loading keys from config file secret.cfg
config = configparser.ConfigParser()
config.read_file(open('/home/sam/accomplishments/api-management-binance/secret.cfg'))
test_api_key = config.get('BINANCE', 'TEST_API_KEY')
test_secret_key = config.get('BINANCE', 'TEST_SECRET_KEY')
actual_api_key = config.get('BINANCE', 'ACTUAL_API_KEY')
actual_api_secret_key = config.get('BINANCE', 'ACTUAL_SECRET_KEY')

client = Client(actual_api_key, actual_api_secret_key)

# client.API_URL = 'https://testnet.binance.vision/api'  # To change endpoint URL for test account 
# client.API_URL = 'https://api.binance.com/api/'

#Get symbol information
info_tings = client.get_symbol_info('BNBBTC')
print(info_tings)

#Get kline candlesticks
candles__s = client.get_klines(symbol='BNBBTC', interval=Client.KLINE_INTERVAL_30MINUTE)

print(candles__s)


info = client.get_account()  # Getting account info

# print(info)

pprint.pprint(info)

# x = info.get('asset')

# print(x)






exchange_info = client.get_exchange_info()
for s in exchange_info['symbols']:
    print(s['symbol'])

# get market depth
# depth = client.get_order_book(symbol='BNBBTC')

# print(depth)

# place a test market buy order, to place an actual order use the create_order function

# order = client.create_test_order(
# symbol='BNBBTC',
# side=Client.SIDE_BUY,
# type=Client.ORDER_TYPE_MARKET, quantity=100)

# get all symbol prices
# prices = client.get_all_tickers()


# Here we are using a for loop to extract the data from a dictionary inside of lists.
for element in prices:
    pprint.pprint((element['symbol']))

coins = pprint.pprint(prices[0]['symbol'])






# withdraw 100 ETH
# check docs for assumptions around withdrawals
# from binance.exceptions import BinanceAPIException
# try:
#     result = client.withdraw(asset='ETH',address='<eth_address>', amount=100)

# Get information of coins (available for deposit and withdraw) for user
info = client.get_all_tickers()
# print(info)

# fetch list of withdrawals
# withdraws = client.get_withdraw_history()
# fetch list of ETH withdrawals
# eth_withdraws = client.get_withdraw_history(coin='ETH')
# get a deposit address for BTC
# address = client.get_deposit_address(coin='BTC')

# async def main():

#     client = await AsyncClient.create()
#     exchange_info = await client.get_exchange_info()
#     tickers = await client.get_all_tickers()

# if __name__ == "__main__":

#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())