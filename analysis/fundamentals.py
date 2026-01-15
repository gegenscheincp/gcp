import yfinance as yf

def get_fundamentals(ticker):
    """
    Fetch key fundamental metrics for a stock.
    Returns a dictionary safe for Streamlit display.
    """

    stock = yf.Ticker(ticker)
    info = stock.info

    fundamentals = {
        "Company": info.get("shortName"),
        "Sector": info.get("sector"),
        "Market Cap": info.get("marketCap"),
        "PE Ratio (TTM)": info.get("trailingPE"),
        "Forward PE": info.get("forwardPE"),
        "PEG Ratio": info.get("pegRatio"),
        "Price to Book": info.get("priceToBook"),
        "Revenue Growth": info.get("revenueGrowth"),
        "Profit Margin": info.get("profitMargins"),
        "ROE": info.get("returnOnEquity"),
        "Debt to Equity": info.get("debtToEquity"),
        "Free Cash Flow": info.get("freeCashflow"),
        "Dividend Yield": info.get("dividendYield"),
        "Dividend Rate": info.get("dividendRate"),
        "Payout Ratio": info.get("payoutRatio"),
    }

    return fundamentals