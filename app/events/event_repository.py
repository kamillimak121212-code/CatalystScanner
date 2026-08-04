from typing import List

from app.models.event import Event


class EventRepository:

    def __init__(self):

        self.events: List[Event] = []

    def add(
        self,
        event: Event
    ):

        self.events.append(event)

        return event

    def get_active_events(
        self,
        company
    ):

        return [

            event

            for event in self.events

            if (
                event.company.ticker == company.ticker
                and event.status == "ACTIVE"
            )

        ]

    def get_all(self):

        return self.events

    def close(
        self,
        event: Event
    ):

        event.status = "CLOSED"

        return event