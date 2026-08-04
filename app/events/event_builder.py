from app.models.event import Event


class EventBuilder:

    def create(

        self,

        evidence

    ):

        understanding = evidence.understanding

        if understanding:

            event_type = understanding.event_type
            summary = understanding.summary

        else:

            event_type = "UNKNOWN"
            summary = evidence.description

        event = Event(

            company=evidence.company,

            event_type=event_type,

            title=evidence.title,

            summary=summary

        )

        event.add_evidence(
            evidence
        )

        return event

    def attach(

        self,

        event,

        evidence

    ):

        event.add_evidence(
            evidence
        )

        return event