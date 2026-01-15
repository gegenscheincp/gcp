from sklearn.ensemble import RandomForestClassifier

def ai_momentum_score(df):
    df = df.dropna()
    df["Target"] = (df["Close"].shift(-5) > df["Close"]).astype(int)

    X = df[["RSI", "SMA50", "SMA200"]]
    y = df["Target"]

    model = RandomForestClassifier(n_estimators=200)
    model.fit(X, y)

    prob = model.predict_proba(X.iloc[-1:])[0][1]
    return round(prob * 100, 2)