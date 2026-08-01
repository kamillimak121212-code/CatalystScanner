def is_relevant_news(news, company):

    text = f"{news.title} {news.summary}".lower()

    COMPANY_KEYWORDS = {
        "NVDA": [
            "nvidia",
            "nvda",
            "jensen huang",
            "cuda",
            "geforce",
            "blackwell",
            "h100",
            "gb200",
            "dgx"
        ]
    }

    keywords = COMPANY_KEYWORDS.get(company.ticker, [])

    for keyword in keywords:
        if keyword in text:
            return True

    return False