_events = []


def add_event(event):

    _events.append(event)

    return event


def get_events():

    return _events


def find_matching_event(event, matcher):

    for existing_event in _events:

        if matcher(existing_event, event):
            return existing_event

    return None


def get_or_create_event(event, matcher):

    existing = find_matching_event(event, matcher)

    if existing:
        return existing

    return add_event(event)