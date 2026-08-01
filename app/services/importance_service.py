from app.models.evidence import EvidenceImportance


HIGH_KEYWORDS = [
    "partnership",
    "acquisition",
    "merger",
    "earnings",
    "record revenue",
    "record profit",
    "guidance",
    "blackwell",
    "cuda",
    "jensen huang",
    "h100",
    "gb200",
    "ceo",
    "contract",
    "deal"
]


MEDIUM_KEYWORDS = [
    "upgrade",
    "downgrade",
    "price target",
    "forecast",
    "launch",
    "ai",
    "chip",
    "gpu",
    "datacenter"
]


LOW_KEYWORDS = [
    "market today",
    "stock market",
    "nasdaq",
    "dow jones",
    "s&p 500"
]


def calculate_importance(news, relevance):

    if relevance < 30:
        return EvidenceImportance.LOW

    text = f"{news.title} {news.summary}".lower()

    for keyword in HIGH_KEYWORDS:
        if keyword in text:
            return EvidenceImportance.HIGH

    for keyword in MEDIUM_KEYWORDS:
        if keyword in text:
            return EvidenceImportance.MEDIUM

    for keyword in LOW_KEYWORDS:
        if keyword in text:
            return EvidenceImportance.LOW

    return EvidenceImportance.MEDIUM