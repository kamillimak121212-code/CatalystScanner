CIK_MAP = {
    "NVDA": "1045810",
    "MSFT": "0789019",
    "AAPL": "0320193",
    "AMD": "0002488",
    "TSLA": "1318605",
    "META": "1326801",
    "AMZN": "1018724",
    "GOOGL": "1652044"
}


def get_cik(ticker):

    return CIK_MAP.get(
        ticker.upper()
    )