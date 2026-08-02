from enum import Enum


class EvidenceSource(Enum):
    RSS = "RSS"
    SEC = "SEC"
    INSIDER = "INSIDER"
    EARNINGS = "EARNINGS"
    ANALYST = "ANALYST"
    MACRO = "MACRO"


class EvidenceImportance(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4


class Evidence:

    def __init__(
        self,
        company,
        source,
        category,
        title,
        description,
        relevance,
        importance,
        url,
        published_at,
        document_text=None
    ):

        self.company = company
        self.source = source
        self.category = category
        self.title = title
        self.description = description
        self.relevance = relevance
        self.importance = importance
        self.url = url
        self.published_at = published_at

        # Full document (SEC, FDA, Earnings itp.)
        self.document_text = document_text

        # AI
        self.understanding = None

        # Signals
        self.signals = []

    def __str__(self):

        return (
            f"[{self.source.value}] "
            f"{self.company.ticker} | "
            f"{self.category}\n"
            f"{self.title}\n"
            f"Relevance: {self.relevance}%\n"
            f"Importance: {self.importance.name if self.importance else 'None'}\n"
            f"Signals: {len(self.signals)}\n"
            f"{self.published_at}"
        )