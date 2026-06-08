# Trading Algorithms

A small collection of quantitative trading scripts implementing common
technical-analysis indicators and a machine-learning approach, in plain Python.

## Scripts

| Script | What it does |
|--------|--------------|
| `algortimo trading medias moviles.py` | Moving-average crossover strategy (buy/sell on MA crosses) |
| `SMA,EMA,RSI(...).py` | Simple & exponential moving averages + **RSI** (relative strength of bullish vs bearish moves) |
| `money flow index algorithm.py` | **Money Flow Index** — volume-weighted momentum oscillator |
| `MACHINE_LEARNING_ALGORITHM.py` | ML-based signal generation on price data |

## What it demonstrates
Technical indicators (SMA/EMA/RSI/MFI), signal generation, and a bridge from classic
rule-based strategies to an ML-driven approach.

## Tech stack
Python · pandas · numpy · (typical: a market-data source / yfinance)

## Use
Each script is standalone — run the one for the strategy you want to explore.
