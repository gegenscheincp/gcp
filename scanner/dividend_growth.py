import yfinance as yf

def dividend_growth_5pct(ticker):
    div = yf.Ticker(ticker).dividends
    if len(div) < 8:
        return False
    yearly = div.resample("Y").sum()
    return yearly.pct_change().mean() >= 0.05