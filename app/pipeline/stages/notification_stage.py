class NotificationStage:

    def process(self, result):

        notify = False

        # Final Decision
        if result.decision is not None:

            if result.decision.recommendation in [
                "STRONG BUY",
                "BUY"
            ]:
                notify = True

        # Fallback
        elif result.prediction is not None:

            if result.prediction.recommendation == "BUY":
                notify = True

        result.should_notify = notify

        return result