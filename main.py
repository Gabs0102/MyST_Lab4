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

def orderbooks(exchanges,run_time,symbol):
     data = asyncio.run(multi_orderbooks(exchanges, run_time=run_time, symbol=symbol))
     data = [item for sublist in data for item in sublist]
     data = pd.DataFrame(data)

     print(data.head())
     return(data)

#Convertir la data a JSON
# json_data=data.to.to_json(orient='records')

# with open('datos.json') as f:
#    data2=json.load(f)
# df = pd.DataFrame.from_dict(data2)


exchanges = ["bitforex", "huobipro", "bitmart"]
run_time = 20  # seconds
symbol = "ETH/BTC"
df = orderbooks(exchanges,run_time,symbol)
#graficos(df)