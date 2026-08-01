from app.services.signal_builder import (
    build_signals
)


class SignalStage:

    def process(self, result):

        result.signals = build_signals(
            result.evidence
        )

        return result