def parse(
    self,
    html
):

    raise Exception("PARSER WAS CALLED")

    if not html:
        return ""

    soup = BeautifulSoup(
        html,
        "html.parser"
    )

    text = soup.get_text(
        separator=" "
    )

    text = re.sub(
        r"\s+",
        " ",
        text
    ).strip()

    logger.info(
        f"Parsed SEC text length: {len(text)}"
    )

    logger.info(
        f"SEC preview: {text[:300]}"
    )

    return text