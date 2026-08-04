import hashlib


def create_news_hash(
    company,
    title,
    description
):

    text = (
        f"{company.ticker}|"
        f"{title}|"
        f"{description}"
    ).lower()

    return hashlib.sha256(
        text.encode("utf-8")
    ).hexdigest()