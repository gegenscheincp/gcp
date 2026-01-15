def earnings_gap(df, gap=0.05):
    prev_close = df["Close"].iloc[-2]
    today_open = df["Open"].iloc[-1]
    return abs((today_open - prev_close) / prev_close) >= gap