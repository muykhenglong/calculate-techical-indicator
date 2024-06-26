#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 13:33:58 2024

Import OHLCV data and calculate Bollinger Bands technical indicator

@author: s.o
"""

import yfinance as yf

tickers = ['AMZN','GOOG','MSFT']

ohclv_data = {}

for ticker in tickers: 
    temp = yf.download(ticker,period='1mo',interval='5m')
    temp.dropna(how='any',inplace=True)
    ohclv_data[ticker] = temp

def Boll_Band(DF, n=14):
    df = DF.copy()
    df['MB'] = df['Adj Close'].rolling(n).mean()
    df['UB'] = df['MB'] + 2*df['Adj Close'].rolling(n).std(ddof=0)
    df['LB'] = df['MB'] - 2*df['Adj Close'].rolling(n).std(ddof=0)
    df['BB_Width'] = df['UB'] - df['LB']
    return df[['MB','UB','LB','BB_Width']]

for ticker in tickers:
    ohclv_data[ticker][['MB','UB','LB','BB_Width']] = Boll_Band(ohclv_data[ticker])