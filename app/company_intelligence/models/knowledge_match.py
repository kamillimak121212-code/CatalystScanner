class KnowledgeMatch:

    def __init__(
        self,
        name,
        category,
        importance,
        source
    ):

        self.name = name
        self.category = category
        self.importance = importance
        self.source = source

    def __repr__(self):

        return (
            f"{self.name} "
            f"[{self.category}] "
            f"{self.source} "
            f"({self.importance})"
        )