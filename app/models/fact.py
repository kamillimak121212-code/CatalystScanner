class Fact:

    def __init__(
        self,
        subject="",
        action="",
        target="",
        value=None,
        confidence=0
    ):

        self.subject = subject
        self.action = action
        self.target = target
        self.value = value
        self.confidence = confidence

    def __str__(self):

        return (
            f"{self.subject} "
            f"{self.action} "
            f"{self.target}"
        )