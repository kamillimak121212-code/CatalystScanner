class Person:

    def __init__(
        self,
        name: str,
        aliases=None,
        importance: int = 50
    ):

        self.name = name
        self.aliases = aliases or []
        self.importance = importance

    def all_names(self):

        return [self.name] + self.aliases

    def matches(self, text: str):

        text = text.lower()

        for name in self.all_names():
            if name.lower() in text:
                return True

        return False