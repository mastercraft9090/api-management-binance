import requests 
import smtplib
from binance.client import Client
import configparser
import json
import os
import time
import pprint
import numpy as np
from threading import Thread
from binance.enums import *
# from bfxhfindicators import
import urllib.request
import asyncio
from binance import AsyncClient

#Loading keys from config file secret.cfg
config = configparser.ConfigParser()
config.read_file(open('/home/sam/accomplishments/api-management-binance/secret.cfg'))
test_api_key = config.get('BINANCE', 'TEST_API_KEY')
test_secret_key = config.get('BINANCE', 'TEST_SECRET_KEY')
actual_api_key = config.get('BINANCE', 'ACTUAL_API_KEY')
actual_api_secret_key = config.get('BINANCE', 'ACTUAL_SECRET_KEY')
username = config.get('BINANCE','USERNAME')
email_password = config.get('BINANCE','PASSWORD')

url = "https://api.binance.com/api/v3/ticker/bookTicker"

#################################################
# server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
# server.login("username","email_password")
# server.sendmail("email", "mastercraft9090@gmail.com", "Whats up G!")
# server.set_debuglevel(1)
# server.quit()

# This code initializes the client, without it the client is not defined
client = Client(actual_api_key, actual_api_secret_key)

# client.API_URL = 'https://testnet.binance.vision/api'  # To change endpoint URL for test account, we do not need this piece of code if we are using the main network.

#######################################
# This gets the EXCHANGE info, a lot of this will be found in the documentation.
# info = client.get_exchange_info()
# print(info)

# This gets info about a specific pair and here we can see the order types that are allowed, we can see Max algo orders, and we can see data is refreshed every 5 mins.
# info = client.get_symbol_info('BNBUSDT')
# pprint.pprint(info)

# Gets all the information about all the tickers available for trade
# info = client.get_all_tickers()
# pprint.pprint(info)
# asset_price = info()


# !This shows my account snapshot and any given time - ! means that we are going to use this in our script.
info = client.get_account_snapshot(type='SPOT')
pprint.pprint(info)

#This are the bid and ask prices for a particular asset.
# depth = client.get_order_book(symbol='BNBUSDT')
# pprint.pprint(depth)

# These are trades that other market participants have executed. these are the most recent ones.
# trades = client.get_recent_trades(symbol='BNBUSDT')
# pprint.pprint(trades)

# candles = client.get_klines(symbol='BNBUSDT', interval=Client.KLINE_INTERVAL_30MINUTE)
# pprint.pprint(candles)

# klines = client.get_historical_klines("ETHBTC", Client.KLINE_INTERVAL_30MINUTE, "1 Jan, 2017", "8 Sep, 2021")
# pprint.pprint(klines)

# First we want to execute trades on the account based upon certain logic
# we want to get the current prices


# This code places an order

# order = client.create_order(
#     symbol='BNBBTC',
#     side=SIDE_BUY,
#     type=ORDER_TYPE_LIMIT,
#     timeInForce=TIME_IN_FORCE_GTC,
#     quantity=100,
#     price='0.00001')

# This code places a limit buy and sell order
# order = client.order_limit_buy(
#     symbol='BNBBTC',
#     quantity=100,
#     price='0.00001')

# order = client.order_limit_sell(
#     symbol='BNBBTC',
#     quantity=100,
#     price='0.00001')

#################################################################
# !if the proce drops below a certain figure, we have to set a stop loss sell. This is the code that we are going to use.
# order = client.create_oco_order(
#     symbol='BNBBTC',
#     side=SIDE_SELL,
#     stopLimitTimeInForce=TIME_IN_FORCE_GTC,
#     quantity=100,
#     stopPrice='0.00001',
#     price='0.00002')

# We then monitor the price and if it makes a come back we execute a buy

