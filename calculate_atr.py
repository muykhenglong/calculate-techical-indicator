#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 13:16:11 2024

Import OHLCV data and calculate ATR technical indicator

@author: s.o
"""

import yfinance as yf

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

for ticker in tickers:
    ohclv_data[ticker]['ATR'] = ATR(ohclv_data[ticker])