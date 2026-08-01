class Risk:

    def __init__(self):

        self.score = 0

        self.level = "LOW"

        self.reasons = []

    def add(
        self,
        points,
        reason
    ):

        self.score += points

        self.reasons.append(reason)

        if self.score >= 60:
            self.level = "HIGH"

        elif self.score >= 30:
            self.level = "MEDIUM"

        else:
            self.level = "LOW"

    def __str__(self):

        reasons = "\n".join(
            f"- {reason}"
            for reason in self.reasons
        )

        if not reasons:
            reasons = "None"

        return (
            f"Score   : {self.score}\n"
            f"Level   : {self.level}\n"
            f"Reasons :\n{reasons}"
        )