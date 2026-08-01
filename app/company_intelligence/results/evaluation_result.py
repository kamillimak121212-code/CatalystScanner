class EvaluationResult:

    def __init__(self):

        self.score = 0
        self.matches = []
        self.categories = set()
        self.total_importance = 0

    @property
    def relevance(self):
        return min(self.score, 100)

    @property
    def category_count(self):
        return len(self.categories)

    @property
    def matched_names(self):
        return [
            match["item"].name
            for match in self.matches
        ]

    def has(self, name):

        name = name.lower()

        return any(
            match["item"].name.lower() == name
            for match in self.matches
        )

    def add_match(self, category, item):

        self.matches.append({
            "category": category,
            "item": item
        })

        self.categories.add(category)

        self.score += item.importance
        self.total_importance += item.importance

    def __str__(self):

        lines = []

        lines.append(f"Relevance: {self.relevance}%")
        lines.append(f"Knowledge Score: {self.total_importance}")
        lines.append(f"Categories: {self.category_count}")
        lines.append("")
        lines.append("Matched Items:")

        for match in self.matches:

            item = match["item"]

            lines.append(
                f"[{match['category']}] "
                f"{item.name} "
                f"(+{item.importance})"
            )

            if item.reason:
                lines.append(f"   ↳ {item.reason}")

        return "\n".join(lines)