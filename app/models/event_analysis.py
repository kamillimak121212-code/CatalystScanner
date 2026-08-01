class EventAnalysis:

    def __init__(self):

        self.evidence_count = 0
        self.high_importance = 0
        self.critical_importance = 0
        self.average_relevance = 0
        self.average_importance = 0
        self.score = 0
        self.confidence = 0
        self.status = "NEW"

    def __str__(self):

        return (
            f"Evidence Count : {self.evidence_count}\n"
            f"High Importance: {self.high_importance}\n"
            f"Critical       : {self.critical_importance}\n"
            f"Avg Relevance  : {self.average_relevance}\n"
            f"Score          : {self.score}\n"
            f"Confidence     : {self.confidence}%\n"
            f"Status         : {self.status}"
        )