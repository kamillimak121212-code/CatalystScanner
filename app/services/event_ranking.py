def rank_events(events):

    return sorted(
        events,
        key=lambda event: event.analysis.score,
        reverse=True
    )