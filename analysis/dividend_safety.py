import yfinance as yf
import numpy as np

def score_payout_ratio(payout):
    if payout is None:
        return 50
    if payout < 0.4:
        return 100
    if payout < 0.6:
        return 80
    if payout < 0.8:
        return 50
    return 20


def score_fcf_coverage(fcf, dividend_rate):
    if not fcf or not dividend_rate:
        return 50
    coverage = fcf / dividend_rate
    if coverage > 2:
        return 100
    if coverage > 1.5:
        return 80
    if coverage > 1:
        return 50
    return 20


def score_debt_equity(de):
    if de is None:
        return 50
    if de < 0.5:
        return 100
    if de < 1:
        return 80
    if de < 2:
        return 50
    return 20


def score_roe(roe):
    if roe is None:
        return 50
    if roe > 0.2:
        return 100
    if roe > 0.15:
        return 80
    if roe > 0.1:
        return 60
    return 30


def score_dividend_growth(dividends):
    if dividends is None or len(dividends) < 8:
        return 40

    yearly = dividends.resample("Y").sum()
    growth = yearly.pct_change().dropna()

    if len(growth) == 0:
        return 40

    avg_growth = growth.mean()

    if avg_growth > 0.08:
        return 100
    if avg_growth > 0.05:
        return 80
    if avg_growth > 0.02:
        return 60
    return 30


def dividend_safety_score(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    dividends = stock.dividends

    payout = info.get("payoutRatio")
    fcf = info.get("freeCashflow")
    dividend_rate = info.get("dividendRate")
    debt_equity = info.get("debtToEquity")
    roe = info.get("returnOnEquity")

    score = (
        score_payout_ratio(payout) * 0.25 +
        score_fcf_coverage(fcf, dividend_rate) * 0.25 +
        score_debt_equity(debt_equity) * 0.15 +
        score_roe(roe) * 0.15 +
        score_dividend_growth(dividends) * 0.20
    )

    return round(score, 2)