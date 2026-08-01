class PipelineResult:

    def __init__(self):

        # Input
        self.evidence = None

        # Company Profile (cache)
        self.profile = None

        # AI Understanding
        self.understanding = None

        # Event Classification
        self.event = None

        # Company Intelligence
        self.evaluation = None

        # Trading Signals
        self.signals = []

        # Importance
        self.importance = None

        # Catalyst Engine
        self.catalyst_score = 0

        # History
        self.history_events = []

        # Prediction
        self.prediction = None

        # Risk
        self.risk = None

        # Final Decision
        self.decision = None

        # Notification
        self.should_notify = False