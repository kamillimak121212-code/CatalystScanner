THEMES = {
    "AI Infrastructure": [
        "ai",
        "artificial intelligence",
        "gpu",
        "cuda",
        "blackwell",
        "gb200",
        "h100",
        "h200",
        "datacenter",
        "cloud",
        "hbm",
        "cowos"
    ],

    "Earnings": [
        "earnings",
        "revenue",
        "eps",
        "guidance",
        "quarter",
        "results"
    ],

    "M&A": [
        "acquisition",
        "acquire",
        "merger",
        "buyout"
    ],

    "Share Buyback": [
        "buyback",
        "repurchase",
        "share repurchase"
    ],

    "Insider Buying": [
        "insider",
        "director bought",
        "ceo bought",
        "officer bought"
    ],

    "China Export": [
        "china",
        "export",
        "restriction",
        "ban",
        "license"
    ]
}


def detect_theme(evidence):

    text = (
        f"{evidence.title} "
        f"{evidence.description}"
    ).lower()

    for theme, keywords in THEMES.items():

        for keyword in keywords:

            if keyword in text:
                return theme

    return "General"