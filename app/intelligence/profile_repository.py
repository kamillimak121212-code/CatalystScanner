class ProfileRepository:

    _profiles = {}

    @classmethod
    def get(cls, ticker):

        return cls._profiles.get(ticker)

    @classmethod
    def save(cls, ticker, profile):

        cls._profiles[ticker] = profile

    @classmethod
    def clear(cls):

        cls._profiles.clear()