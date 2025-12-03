import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

url = "https://raw.githubusercontent.com/liaochunyang/PIC16/refs/heads/main/PIC16A/data/timeseries-sample-data.csv"
df = pd.read_csv(url)

dates = np.array(pd.to_datetime(df["dates"]))
symbols = np.array(df["symbols"])
prices = np.array(df["prices"])

symbol_dict = {0: "Gamestop", 1: "AMC", 2: "Exxon"}


def describe(symbol, dates, symbols, prices):
    ix = np.array(symbols == symbol)
    stock_prices, stock_transactions = prices[ix], dates[ix]
    print(f"There are {len(stock_prices)} entries for {symbol}.")
    avg_value = np.mean(stock_prices)
    max_value = np.max(stock_prices)
    print(f"Avg value was {avg_value} and max value was {max_value}")
    earliest = np.min(stock_transactions)
    latest = np.max(stock_transactions)
    print(f"Time period ran from {earliest} to {latest}")


fig, axarr = plt.subplots(3, 1)


def plot_symbols(s, dates, symbols, prices, ax):
    ix = symbols == s
    s_prices, s_transactions = prices[ix], dates[ix]
    dates_ix = np.argsort(s_transactions)
    ax.plot(s_transactions[dates_ix], s_prices[dates_ix])


for i in range(len(axarr)):
    plot_symbols(i, dates, symbols, prices, axarr[i])

plt.show()
