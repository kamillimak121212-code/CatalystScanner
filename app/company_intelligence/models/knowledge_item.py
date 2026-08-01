class KnowledgeItem:

    def __init__(
        self,
        name,
        importance=10,
        aliases=None,
        reason="",
        category="",
        impact="MEDIUM",
        tags=None
    ):

        self.name = name

        self.importance = importance

        self.aliases = aliases or []

        self.reason = reason

        self.category = category

        self.impact = impact

        self.tags = tags or []