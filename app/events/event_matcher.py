from datetime import datetime, timedelta


class EventMatcher:

    MATCH_WINDOW = timedelta(hours=24)

    def match(
        self,
        evidence,
        events
    ):

        understanding = evidence.understanding

        if understanding is None:
            return None

        for event in events:

            if event.event_type != understanding.event_type:
                continue

            if (
                datetime.utcnow() - event.created_at
            ) > self.MATCH_WINDOW:
                continue

            return event

        return None