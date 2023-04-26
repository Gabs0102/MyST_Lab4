#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 08:03:29 2023

@author: gabrielaortiz
"""

import asyncio
import ccxt.async_support as ccxta
import time
import numpy as np
import pandas as pd

if __name__ == "__main__":
     exchanges = ["kucoin", "bittrex", "bitfinex"]
     run_time = 10  # seconds
     symbol = "ETH/BTC"

     data = asyncio.run(multi_orderbooks(exchanges, run_time=run_time, symbol=symbol))
     data = [item for sublist in data for item in sublist]
     data = pd.DataFrame(data)

     print(data.head())