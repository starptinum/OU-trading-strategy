# Pair Trading Using Ornstein–Uhlenbeck Process
## Introduction
This repository contains the code and documentation for an algorithmic trading strategy based on the Ornstein-Uhlenbeck (OU) process in pair trading.

## Methodology
The strategy utilizes the OU process to model price spreads between paired stocks. The spread is the difference between the prices of two securities and is expected to oscillate around its mean value. The OU process parameters ($\theta$, $\mu$, $\sigma$) are estimated using maximum likelihood estimation (MLE) to guide the development of a mean-reverting pair trading strategy.

## Implementation
The implementation involves the following steps:
1. Data Collection: Historical stock price data for the S&P500 universe between 2014 and 2020 is collected from Yahoo Finance.
2. Modelling the Spread: The spread between paired stocks is modelled as an OU process using the stochastic differential equation. The parameters $\theta$, $\mu$, and $\sigma$ are estimated using MLE.
3. Pair Selection: Eligible pairs are chosen based on high positive correlation, stationary spread (Augmented Dickey-Fuller test), and mean reversion (Hurst exponent test).
4. Predicting Spread Returns: An Ordinary Least Squares regression model is trained to predict the spread returns of eligible pairs.
5. Trading Signals: Trading signals are generated based on predicted spread returns and the deviation from the expected mean value.

## Results
During the 3-month testing period, the trading strategy yielded a market-neutral portfolio with a 138% annual return. The strategy achieved a Sharpe ratio of 2.60 and a Calmar ratio of 12.70, with an annualized volatility of 35.7%.

For further details, please refer to the code and documentation in this repository.
