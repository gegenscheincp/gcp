def rsi_oversold(df, level=30):
    return df["RSI"].iloc[-1] < level