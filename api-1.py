#Importing Libraries
from binance.client import Client
import configparser

#Loading keys from config file secret.cfg
config = configparser.ConfigParser()
config.read_file(open('/home/sam/accomplishments/api-management-binance/secret.cfg'))
test_api_key = config.get('BINANCE', 'TEST_API_KEY')
test_secret_key = config.get('BINANCE', 'TEST_SECRET_KEY')

client = Client(test_api_key, test_secret_key)

client.API_URL = 'https://testnet.binance.vision/api'  # To change endpoint URL for test account 

# info = client.get_account()  # Getting account info

# print(info)

# exchange_info = client.get_exchange_info()
# for s in exchange_info['symbols']:
#     print(s['symbol'])

# get market depth
depth = client.get_order_book(symbol='BNBBTC')

# print(depth)

# place a test market buy order, to place an actual order use the create_order function

order = client.create_test_order(
symbol='BNBBTC',
side=Client.SIDE_BUY,
type=Client.ORDER_TYPE_MARKET, quantity=100)

# get all symbol prices
# prices = client.get_all_tickers()

# print(prices)


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