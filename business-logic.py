import requests 
from binance.client import Client
import configparser
import json
import os
import time
import numpy as np
from threading import Thread
# from bfxhfindicators import
import urllib.request
import asyncio
from binance import AsyncClient

#Loading keys from config file secret.cfg
config = configparser.ConfigParser()
config.read_file(open('/home/sam/accomplishments/api-management-binance/secret.cfg'))
test_api_key = config.get('BINANCE', 'TEST_API_KEY')
test_secret_key = config.get('BINANCE', 'TEST_SECRET_KEY')

url = "https://api.binance.com/api/v3/ticker/bookTicker"

async def main():

    client = await AsyncClient.create()
    exchange_info = await client.get_exchange_info()
    tickers = await client.get_all_tickers()

if __name__ == "__main__":

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

response = requests.request("GET", url)
# print(response.text)

BASE_URL = 'https://api.binance.com/'
TIMEFRAME = '4h'

symbols = []
candles = {}
prices = {}

#create a results folder if it does not exist
print('Working with the results folder....')
if not os.path.exists('results/'):
    os.makedirs('results/')

#start with blank files
open('results/below_50.txt', 'w').close()
open('results/above_50_below_200.txt', 'w').close()
open('results/above_200.txt', 'w').close()
open('results/pairs', 'w').close()



usdt_pairs = ()

array = np.array(usdt_pairs),

#Load symbols that have a USDT base pair
print('Getting list of USDT trading pairs....')
resp = requests.get('https://api.binance.com/api/v3/ticker/bookTicker')


tickers_list = json.loads(resp.content)
symbols = []
for ticker in tickers_list:
   
    if str(ticker['symbol'])[-4:] == 'USDT':
       
        symbols.append(ticker['symbol'])
        # print(ticker['symbol'])
            
        # usdt_output.append(usdt_pairs)
        # usdt_list = print(symbols)

usdt_pairs = symbols       
        
        

     


    
# Get the 4h candle data for the above symbols
print('Loading candle data for symbols....')
def load_candles(sym):
    global candles, prices, BASE_URL
    payload = {
        'symbol': sym,
        'interval': '4h',
        'limit': 250
    }

for sym in symbols:
    Thread(target=load_candles, args=(sym,)).start()
while len(candles) < len(symbols):
    print('%s/%s loaded' %(len(candles), len(symbols)), end='\r', flush=True)
    time.sleep(0.1)



# def load_candles(sym):
#     global candles, prices, BASE_URL
#     payload = {
#         'symbol': sym,
#         'interval': '4h',
#         'limit': 250
#     }

resp = requests.get('https://api.binance.com/api/v3/ticker/bookTicker', params=payload)
klines = json.loads(resp.content)
#parse klines and store open, high, low, close and vol only

print('Parsing stored klines....')

parsed_klines = []
for k in klines:
    k_candle = {
        'open': float(k[1]),
        'high': float(k[2]),
        'low': float(k[3]),
        'close': float(k[4]),
        'vol': float(k[5])
    }
    parsed_klines.append(k_candle)
candles[sym] = parsed_klines
index = len(parsed_klines) - 1 # get the index of the latest candle
prices[sym] = parsed_klines[index]['close'] # save the current price
# calculate EMAs for each symbol
print('Calculating EMAs...')
for sym in candles:
    for period in EMA_PERIODS:
        iEMA = EMA([period])
        lst_candles = candles[sym][:]
        for c in lst_candles:
            iEMA.add(c['close'])
        if sym not in ema_values:
            ema_values[sym] = {}
        ema_values[sym][period] = iEMA.v()

# save filtered EMA results in txt files
print('Saving filtered EMA results to txt files...')
for sym in ema_values:
    ema_50 = ema_values[sym][50]
    ema_200 = ema_values[sym][200]
    price = prices[sym]
    entry = ''
    if price < ema_50:
    # save symbols trading below EMA (50)
        f = open('results/below_50.txt', 'a')
        entry = '%s: $%s\n' %(sym, round(price,3))
        f.write(entry)
    elif price > ema_50 and price < ema_200:
    # save symbols trading above EMA(200)
        f = open('results/above_50_below_200.txt', 'a')
        entry = '%s: $%s\n' %(sym, round(price,3))
        f.write(entry)
    elif price > ema_200:
    # save symbols trading above EMA(50) but below EMA(200)
        f = open('results/above_200.txt', 'a')
        entry = '%s: $%s\n' %(sym, round(price,3))
        f.write(entry)
    f.close()
    del f # cleanup

print('All done! Results saved in results folder.')

# #kijun-sen

# def kijun_sen(Data, close, high, low, kijun_lookback, where):
    
#     for i in range(len(Data)):
#         try:
#             Data[i, where] = max(Data[i - kijun_lookback:i + 1, high]) + min(Data[i - kijun_lookback:i + 1, low])
    
#         except ValueError:
#             pass
        
#     Data[:, where] = Data[:, where] / 2
    
#     return Data