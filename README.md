# Technical Indicators Calculation Repository

This repository contains a collection of Python scripts designed to calculate various technical indicators used in financial markets analysis. Each script is dedicated to a specific indicator, providing tools for traders and analysts to integrate and utilize in market analysis or trading strategies.

## Indicators Included

The repository includes scripts for the following technical indicators:

- **ADX (Average Directional Index)**: Measures the strength of a trend.
- **ATR (Average True Range)**: Provides insights into market volatility.
- **Bollinger Bands**: Used to determine overbought and oversold conditions.
- **MACD (Moving Average Convergence Divergence)**: Identifies changes in the strength, direction, momentum, and duration of a trend in a stock's price.
- **Renko Charts**: Focuses on price changes of a predetermined magnitude, filtering out small price movements.
- **RSI (Relative Strength Index)**: Measures the speed and change of price movements.


- **ADX (Average Directional Index)**: Measures the strength of a trend irrespective of its direction. Values above 25 often indicate a strong trend, while values below 20 suggest a weak trend. This indicator is useful for determining whether a market is likely to continue in its current trend or not.

The ADX is derived from two other indicators, also developed by Welles Wilder, called the Positive Directional Indicator (+DI) and Negative Directional Indicator (-DI). The ADX is the smoothed moving average of the absolute value of "+DI minus -DI" divided by "+DI plus -DI", all multiplied by 100. It is designed to measure the strength of a trend without regard to its direction.

- **ATR (Average True Range)**: Provides insights into market volatility by measuring the degree of price volatility from high to low for each period, adjusted for gaps in price movement. Higher ATR values indicate increased volatility, which can be crucial for adjusting trading strategies or positioning stop-loss orders.

The ATR is calculated by taking the average of true ranges over a specified period. A true range is defined as the greatest of the following: 
-- The difference between the current high and the current low.
-- The absolute value of the current high less the previous close.
-- The absolute value of the current low less the previous close.

- **Bollinger Bands**: Consists of a middle band being a moving average, with two outer bands calculated based on standard deviations from the middle band. This indicator is used to determine overbought and oversold conditions in the market. Prices near the upper band suggest that an asset may be overbought, while prices near the lower band can indicate an asset is oversold.

Bollinger Bands consist of:
-- A middle band being a simple moving average (SMA) of closing prices, typically over the last 20 days.
-- An upper band at K times an N-period standard deviation above the middle band (SMA + K*standard deviation).
-- A lower band at K times an N-period standard deviation below the middle band (SMA - K*standard deviation),
where N and K are usually 20 and 2, respectively.

- **MACD (Moving Average Convergence Divergence)**: A trend-following momentum indicator that shows the relationship between two moving averages of a security’s price. The MACD is calculated by subtracting the 26-period Exponential Moving Average (EMA) from the 12-period EMA. The result of this calculation is the MACD line. A nine-day EMA of the MACD called the "signal line," is then plotted on top of the MACD line, which can function as a trigger for buy and sell signals.

- **Renko Charts**: Utilizes price movement that meets or exceeds a specified amount to plot a brick on a chart. Bricks are only added when price movements are larger than a predefined amount, thereby filtering out smaller price changes. This makes trends easier to spot in a visual analysis.

- **RSI (Relative Strength Index)**: A momentum oscillator that measures the speed and change of price movements on a scale of 0 to 100. Typically, RSI is used to identify overbought or oversold conditions. An RSI above 70 is generally considered overbought, while an RSI below 30 is considered oversold. This indicator is commonly used to predict the future direction of market prices.

RSI is calculated using the following formula:
-- RSI = 100 - (100 / (1 + RS)),
where RS (Relative Strength) is the average of 'x' days' up closes divided by the average of 'x' days' down closes.

## Requirements

Python 3.8.19

## Author

Muykheng Long - https://github.com/muykhenglong/
