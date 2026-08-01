import yfinance as yf


class PriceDownloader:

    def download(self, ticker):

        stock = yf.Ticker(ticker)

        history = stock.history(
            period="2y",
            auto_adjust=True
        )

        return history