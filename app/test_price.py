from app.history.price_downloader import PriceDownloader


downloader = PriceDownloader()

history = downloader.download("NVDA")

print(history.head())

print()

print(history.tail())