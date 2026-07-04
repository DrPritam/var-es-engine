import yfinance as yf
import pandas as pd

def download_prices(tickers, start, end):
    raw = yf.download(tickers, start=start, end=end)
    prices = raw["Close"]
    prices = prices.dropna()
    return prices
if __name__ == "__main__":
    tickers = ["SPY", "QQQ", "GLD", "TLT", "EEM"]
    df = download_prices(tickers, "2019-01-01", "2026-06-30")
    print(df.shape)
    print(df.head())
    df.to_csv("data/prices.csv")
    