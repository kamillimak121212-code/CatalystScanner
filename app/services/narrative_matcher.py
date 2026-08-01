def find_matching_narrative(
    understanding,
    narratives
):

    for narrative in narratives:

        if narrative.title == understanding.event:
            return narrative

    return None