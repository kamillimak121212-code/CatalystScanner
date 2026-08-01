from app.models.company_profile import CompanyProfile


def get_profile():

    profile = CompanyProfile()

    profile.business = (
        "Designs GPUs and AI computing platforms."
    )

    profile.products = [
        "Blackwell",
        "Rubin",
        "CUDA",
        "DGX",
        "NVLink",
        "TensorRT"
    ]

    profile.customers = [
        "Microsoft",
        "Amazon",
        "Google",
        "Meta",
        "Oracle",
        "OpenAI",
        "CoreWeave",
        "Tesla",
        "xAI"
    ]

    profile.suppliers = [
        "TSMC",
        "SK Hynix",
        "Micron"
    ]

    profile.competitors = [
        "AMD",
        "Intel"
    ]

    profile.catalysts = [
        "AI CapEx",
        "GPU Demand",
        "HBM",
        "CoWoS",
        "AI Datacenters",
        "Earnings",
        "Guidance",
        "Export Restrictions"
    ]

    return profile