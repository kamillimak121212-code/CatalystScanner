from app.company_intelligence.nvda_profile import NvidiaProfile


class ProfileManager:

    _profiles = {
        "NVDA": NvidiaProfile()
    }

    @classmethod
    def get_profile(cls, ticker):

        return cls._profiles.get(ticker)