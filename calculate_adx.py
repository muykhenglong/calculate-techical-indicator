#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 15:26:11 2024

Import OHLCV data and calculate ADX technical indicator

@author: s.o
"""

import yfinance as yf
import numpy as np

tickers = ['AMZN','GOOG','MSFT']

ohclv_data = {}

for ticker in tickers: 
    temp = yf.download(ticker,period='1mo',interval='5m')
    temp.dropna(how='any',inplace=True)
    ohclv_data[ticker] = temp
    
def ATR(DF, n=14):
    df = DF.copy()
    df['H-L'] = df['High'] - df['Low']
    df['H-PC'] = df['High'] - df['Adj Close'].shift(1)
    df['L-PC'] = df['Low'] - df['Adj Close'].shift(1)
    df['TR'] = df[['H-L','H-PC','L-PC']].max(axis=1)
    df['ATR'] = df['TR'].ewm(com=n, min_periods=n).mean()
    return df['ATR']    

def ADX(DF,n=20):
    df = DF.copy()
    df['ATR'] = ATR(df,n)
    df['upmove'] = df['High'] - df['High'].shift(1)
    df['downmove'] = df['Low'].shift(1) - df['Low']
    df['+dm'] = np.where((df['upmove']>df['downmove']) & (df['upmove']>0), df['upmove'], 0)
    df['-dm'] = np.where((df['upmove']<df['downmove']) & (df['downmove']>0), df['downmove'], 0)
    df['+di'] = 100 * (df['+dm']/df['ATR']).ewm(com=n, min_periods=n).mean() #use com because it seems to provide closer ADX values to yahoo finance chart than span
    df['-di'] = 100 * (df['-dm']/df['ATR']).ewm(com=n, min_periods=n).mean()
    df['ADX'] = 100 * abs((df['+di'] - df['-di'])/(df['+di'] + df['-di'])).ewm(com=n, min_periods=n).mean()
    return df['ADX']
    
for ticker in tickers:
    ohclv_data[ticker]['ADX'] = ADX(ohclv_data[ticker],20)