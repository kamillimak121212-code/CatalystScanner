class CompanyRelation:

    def __init__(
        self,
        company: str,
        relation: str,
        aliases=None,
        importance: int = 50
    ):

        self.company = company
        self.relation = relation
        self.aliases = aliases or []
        self.importance = importance

    def all_names(self):

        return [self.company] + self.aliases

    def matches(self, text: str):

        text = text.lower()

        for name in self.all_names():
            if name.lower() in text:
                return True

        return False