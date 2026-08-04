import hashlib


def create_news_hash(
    title,
    summary,
    url
):

    text = (
        f"{title}|"
        f"{summary}|"
        f"{url}"
    ).lower()

    return hashlib.sha256(
        text.encode("utf-8")
    ).hexdigest()