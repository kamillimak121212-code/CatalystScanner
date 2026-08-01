from app.models.event_type import EventType


class EventClassificationStage:

    def process(self, result):

        understanding = result.understanding

        if understanding is None:

            result.event = None

            return result

        try:

            event_type = EventType(
                understanding.event_type
            )

        except Exception:

            event_type = EventType.UNKNOWN

        result.event = {

            "event_type": event_type,

            "sentiment": understanding.sentiment,

            "confidence": understanding.confidence,

            "summary": understanding.summary,

            "is_relevant": understanding.is_relevant

        }

        return result