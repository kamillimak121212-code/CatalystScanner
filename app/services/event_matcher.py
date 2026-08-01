import re

STOP_WORDS = {
    "the", "a", "an", "to", "of", "and", "for",
    "in", "on", "with", "by", "is", "are", "at",
    "this", "that", "today"
}


def normalize(text):

    words = re.findall(r"\w+", text.lower())

    return {
        word
        for word in words
        if len(word) > 2 and word not in STOP_WORDS
    }


def is_same_event(event1, event2):

    if event1.company.ticker != event2.company.ticker:
        return False

    if event1.theme != event2.theme:
        return False

    words1 = normalize(event1.title)
    words2 = normalize(event2.title)

    common = words1 & words2

    return len(common) >= 2