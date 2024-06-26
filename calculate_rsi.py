#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 15:03:32 2024

Import OHLCV data and calculate RSI technical indicator

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

def RSI(DF,n=14):
    df= DF.copy()
    df['change'] = df['Adj Close'] - df['Adj Close'].shift(1)
    df['gain'] = np.where(df['change']>=0,df['change'],0)
    df['loss'] = np.where(df['change']<0,-1*df['change'],0)
    df['avgGain'] = df['gain'].ewm(alpha=1/n, min_periods=n).mean()
    df['avgLoss'] = df['loss'].ewm(alpha=1/n, min_periods=n).mean()
    df['rs'] = df['avgGain']/df['avgLoss']
    df['rsi'] = 100 - 100/(1+df['rs'])
    return df['rsi']

for ticker in tickers:
    ohclv_data[ticker]['rsi'] = RSI(ohclv_data[ticker])