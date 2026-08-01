class Signal:

    def __init__(
        self,
        signal_type="",
        value="",
        source="",
        importance=0,
        confidence=0,
        reason=""
    ):

        self.signal_type = signal_type

        self.value = value

        self.source = source

        self.importance = importance

        self.confidence = confidence

        self.reason = reason

    def __str__(self):

        return (
            f"Type       : {self.signal_type}\n"
            f"Value      : {self.value}\n"
            f"Source     : {self.source}\n"
            f"Importance : {self.importance}\n"
            f"Confidence : {self.confidence}\n"
            f"Reason     : {self.reason}"
        )