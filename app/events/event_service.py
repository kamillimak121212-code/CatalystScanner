from app.events.event_builder import EventBuilder
from app.events.event_matcher import EventMatcher
from app.events.event_repository import EventRepository


class EventService:

    def __init__(self):

        self.repository = EventRepository()

        self.matcher = EventMatcher()

        self.builder = EventBuilder()

    def process(

        self,

        evidence

    ):

        events = self.repository.get_active_events(
            evidence.company
        )

        event = self.matcher.match(
            evidence,
            events
        )

        if event:

            return self.builder.attach(
                event,
                evidence
            )

        event = self.builder.create(
            evidence
        )

        self.repository.add(
            event
        )

        return event