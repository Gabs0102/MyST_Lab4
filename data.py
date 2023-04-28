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


async def async_client(exchange_id, run_time: int, symbol: str):
    orderbook = None
    ohlc = None
    exchange = getattr(ccxta, exchange_id)()
    time_1 = time.time()
    time_f = 0
    ob = []
    while time_f <= run_time:
        try:
            await exchange.load_markets()
            market = exchange.market(symbol)
            await asyncio.sleep(15)
            orderbook = await exchange.fetch_order_book(market["symbol"])
            ohlc = await exchange.fetch_ohlcv(market["symbol"], timeframe='1m')
            datetime = exchange.iso8601(exchange.milliseconds())
            ask_volume=sum([row[1] for row in orderbook['asks']])
            bid_volume=sum([row[1] for row in orderbook['bids']])
            total_vol=ask_volume+bid_volume
            ask_price = orderbook['asks'][0][0]
            bid_price = orderbook['bids'][0][0]
            mid_price = (ask_price+bid_price)/2
            ask_vwap=0
            bid_vwap=0
            for ask in orderbook['asks']:
                price=ask[0]
                volume=ask[1]
                ask_vwap+=price*volume/ask_volume
            for bid in orderbook['asks']:
                price=bid[0]
                volume=bid[1]
                bid_vwap+=price*volume/bid_volume
            vwap=(ask_vwap*ask_volume+bid_vwap*bid_volume)/total_vol
            spread = ask_price-bid_price
           #datos ohlc 
            open_price=ohlc[-1][1]
            high_price=max([row[2] for row in ohlc])
            low_price=min([row[3] for row in ohlc])
            close_price=ohlc[-1][4]
            delta_p=np.diff([row[4]for row in ohlc], prepend=open_price)
            delta_p_l=np.roll(delta_p,60)
            cov=np.cov([delta_p,delta_p_l])[0][1]
            effective_spread=abs(spread)+abs(cov)
            # Final data format for the results
            ob.append(
                {
                    "exchange": exchange_id,
                    "timeStamp": datetime,
                    "Level": len(orderbook['asks']),
                    "ask_volume": ask_volume,
                    "bid_volume": bid_volume,
                    "total_vol":total_vol,
                    "mid_price":mid_price,
                    "vwap":vwap,
<<<<<<< HEAD
                    "close_price": close_price,
                    "spread":spread,
                    "effective_spread":effective_spread,
            )
            # End time
            time_2 = time.time()
            time_f = round(time_2 - time_1, 4)
        except Exception as e:
            time_2 = time.time()
            time_f = round(time_2 - time_1, 4)
            print(type(e).__name__, str(e))
    await exchange.close()
    return ob


async def multi_orderbooks(exchanges, run_time: int, symbol: str):
    input_coroutines = [
        async_client(exchange, run_time, symbol) for exchange in exchanges
    ]
    orderbooks = await asyncio.gather(*input_coroutines, return_exceptions=True)
    return orderbooks




