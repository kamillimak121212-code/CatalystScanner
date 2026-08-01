class HistoryReaction:

    def __init__(self):

        # Prices
        self.price_before = None

        self.price_1d = None
        self.price_3d = None
        self.price_5d = None
        self.price_10d = None
        self.price_30d = None
        self.price_90d = None

        # Returns (%)
        self.change_1d = 0.0
        self.change_3d = 0.0
        self.change_5d = 0.0
        self.change_10d = 0.0
        self.change_30d = 0.0
        self.change_90d = 0.0

        # Maximum move
        self.max_gain = 0.0
        self.max_loss = 0.0

        # Final outcome
        self.direction = "UNKNOWN"   # UP / DOWN / FLAT

        # Statistics
        self.volatility = 0.0

        self.volume_change = 0.0