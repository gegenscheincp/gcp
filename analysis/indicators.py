import ta

def add_indicators(df):
    df["RSI"] = ta.momentum.RSIIndicator(df["Close"]).rsi()
    df["SMA50"] = df["Close"].rolling(50).mean()
    df["SMA200"] = df["Close"].rolling(200).mean()
    df["Returns"] = df["Close"].pct_change()
    return df