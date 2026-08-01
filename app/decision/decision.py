class Decision:

    def __init__(self):

        self.score = 0

        self.recommendation = "IGNORE"

        self.reason = ""

    def __str__(self):

        return (
            f"Recommendation : {self.recommendation}\n"
            f"Score          : {self.score}\n"
            f"Reason         : {self.reason}"
        )