#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 12:05:40 2024

Import OHLCV data and calculate MACD technical indicator

@author: s.o
"""

import yfinance as yf

tickers = ['AMZN','GOOG','MSFT']

ohclv_data = {}

for ticker in tickers: 
    temp = yf.download(ticker,period='1mo',interval='15m')
    temp.dropna(how='any',inplace=True)
    ohclv_data[ticker] = temp

def MACD(DF,a=12,b=26,c=9):
    df = DF.copy()
    df['ma_fast'] = df['Adj Close'].ewm(span=a,min_periods=a).mean()
    df['ma_slow'] = df['Adj Close'].ewm(span=b,min_periods=b).mean()
    df['macd'] = df['ma_fast'] - df['ma_slow']
    df['signal'] = df['macd'].ewm(span=c,min_periods=c).mean()
    return df[['macd','signal']]

for ticker in tickers:
    ohclv_data[ticker][['MACD','SIGNAL']] = MACD(ohclv_data[ticker])