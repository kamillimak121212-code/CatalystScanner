class EventQueue:

    def __init__(self):

        self.events = []

    def add(self, evidence):

        self.events.append(
            evidence
        )

    def add_all(self, evidences):

        self.events.extend(
            evidences
        )

    def get_all(self):

        return self.events

    def clear(self):

        self.events.clear()

    def __len__(self):

        return len(
            self.events
        )