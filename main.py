#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: gabrielaortiz
"""

import pandas as pd 
import data
from data import multi_orderbooks
import asyncio
from visualizations import graficos
import numpy as np

def orderbooks(exchanges,run_time,symbol):
     data = asyncio.run(multi_orderbooks(exchanges, run_time=run_time, symbol=symbol))
     data = [item for sublist in data for item in sublist]
     data = pd.DataFrame(data)
     a1= data.loc[:,['exchange', 'timeStamp','Level','ask_volume','bid_volume','total_vol','mid_price','vwap']]
     # print(a1.head())
     a2= data.loc[:,['timeStamp','close_price','spread','effective_spread']]
     # print(a2.head())
     return(data)

#Convertir la data a JSON
# json_data=data.to.to_json(orient='records')

# with open('datos.json') as f:
#    data2=json.load(f)
# df = pd.DataFrame.from_dict(data2)



exchanges = ["bitforex",'bitmex','bitfinex']
run_time = 60*60 # seconds
symbol = "ETH/BTC"
df = (orderbooks(exchanges,run_time,symbol))
df.to_csv(r'files/orderbooks_29abr.csv')
# print(df)
# print(df.info())

# graficos(df)
