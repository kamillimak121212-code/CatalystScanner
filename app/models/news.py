class News:

    def __init__(self, title, summary, url, source, published_at):
        self.title = title
        self.summary = summary
        self.url = url
        self.source = source
        self.published_at = published_at

    def __str__(self):
        return (
        f"Title: {self.title}\n"
        f"Summary: {self.summary}\n"
        f"Source: {self.source}\n"
        f"Published: {self.published_at}\n"
        f"URL: {self.url}"
    )