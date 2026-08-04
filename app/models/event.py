from datetime import datetime


class Event:

    def __init__(

        self,

        company,

        event_type,

        title,

        summary

    ):

        # Identity
        self.id = None

        # Company
        self.company = company

        # Classification
        self.event_type = event_type

        # Description
        self.title = title
        self.summary = summary

        # Timeline
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        self.closed_at = None

        # State
        self.status = "ACTIVE"

        # Evidence
        self.evidence = []

        # Scores
        self.priority = 0
        self.confidence = 0

        # AI
        self.ai_summary = None

        # History
        self.price_reaction = None

        # Statistics
        self.similar_events = []

    def add_evidence(

        self,

        evidence

    ):

        self.evidence.append(
            evidence
        )

        self.updated_at = datetime.utcnow()