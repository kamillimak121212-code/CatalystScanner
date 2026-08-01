from datetime import date, timedelta

from app.api.finnhub.client import (
    FinnhubClient
)


def main():

    client = FinnhubClient()

    news = client.get_company_news(
        ticker="AAPL",
        from_date=(
            date.today() - timedelta(days=30)
        ).isoformat(),
        to_date=date.today().isoformat()
    )

    print(f"\nFound {len(news)} news\n")

    for article in news[:5]:

        print("=" * 80)

        print(article["headline"])

        print(article["datetime"])

        print(article["source"])

        print(article["url"])


if __name__ == "__main__":

    main()