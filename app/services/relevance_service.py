from app.company_intelligence.profile_manager import ProfileManager


def calculate_relevance(news, company):

    profile = ProfileManager.get_profile(company.ticker)

    if profile is None:
        return 0

    result = profile.evaluate(news)

    print("\n==============================")
    print("COMPANY INTELLIGENCE")
    print("==============================")
    print(result)

    return result.relevance