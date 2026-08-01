from app.company_intelligence.base_profile import CompanyProfile
from app.company_intelligence.models.knowledge_item import KnowledgeItem


class NvidiaProfile(CompanyProfile):

    def __init__(self):

        super().__init__()

        self.people = [

    KnowledgeItem(
        name="Jensen Huang",
        importance=100,
        category="Person",
        impact="CRITICAL",
        reason=(
            "Founder and CEO of NVIDIA. His strategic vision, product launches, "
            "earnings commentary and AI roadmap frequently influence NVIDIA's "
            "stock price and long-term valuation."
        ),
        tags=[
            "CEO",
            "Leadership",
            "AI",
            "GPU",
            "Keynote",
            "Strategy"
        ]
    ),

    KnowledgeItem(
        name="Colette Kress",
        importance=90,
        category="Person",
        impact="HIGH",
        reason=(
            "Chief Financial Officer. Responsible for financial guidance, "
            "capital allocation, margins and quarterly earnings commentary."
        ),
        tags=[
            "CFO",
            "Finance",
            "Margins",
            "Guidance",
            "Earnings"
        ]
    )

]

        self.products = [

    KnowledgeItem(
        name="Blackwell",
        importance=100,
        aliases=[
            "GB200",
            "B200",
            "Blackwell Ultra"
        ],
        category="Product",
        impact="CRITICAL",
        reason=(
            "Current flagship AI GPU architecture. Blackwell is expected "
            "to drive NVIDIA's datacenter revenue for the coming years. "
            "Production, customer adoption and supply constraints have a "
            "direct impact on revenue, margins and valuation."
        ),
        tags=[
            "AI",
            "GPU",
            "Datacenter",
            "Training",
            "Inference",
            "Blackwell"
        ]
    ),

    KnowledgeItem(
        name="Hopper",
        importance=95,
        aliases=[
            "H100",
            "H200",
            "HGX"
        ],
        category="Product",
        impact="CRITICAL",
        reason=(
            "Previous flagship AI GPU architecture still widely deployed "
            "by hyperscalers and enterprise customers."
        ),
        tags=[
            "AI",
            "GPU",
            "Datacenter"
        ]
    ),

    KnowledgeItem(
        name="Rubin",
        importance=95,
        category="Product",
        impact="CRITICAL",
        reason=(
            "Next-generation GPU architecture on NVIDIA's roadmap. "
            "Any news regarding Rubin may significantly change long-term "
            "growth expectations."
        ),
        tags=[
            "Roadmap",
            "AI",
            "GPU"
        ]
    ),

    KnowledgeItem(
        name="CUDA",
        importance=100,
        category="Technology",
        impact="CRITICAL",
        reason=(
            "CUDA is NVIDIA's proprietary software platform and one of "
            "its strongest competitive advantages."
        ),
        tags=[
            "Software",
            "AI",
            "Platform",
            "Developer Ecosystem"
        ]
    ),

    KnowledgeItem(
        name="DGX",
        importance=90,
        category="Product",
        impact="HIGH",
        reason=(
            "Enterprise AI supercomputer platform used to train "
            "large language models and other advanced AI systems."
        ),
        tags=[
            "Enterprise",
            "AI",
            "Datacenter"
        ]
    ),

    KnowledgeItem(
        name="Grace",
        importance=80,
        aliases=[
            "Grace CPU",
            "Grace Hopper"
        ],
        category="Product",
        impact="HIGH",
        reason=(
            "ARM-based CPU platform designed for AI computing and "
            "high-performance datacenters."
        ),
        tags=[
            "CPU",
            "Datacenter",
            "AI"
        ]
    ),

    KnowledgeItem(
        name="RTX",
        importance=70,
        category="Product",
        impact="MEDIUM",
        reason=(
            "GPU family serving gaming, creator and workstation markets."
        ),
        tags=[
            "Gaming",
            "Workstation",
            "Graphics"
        ]
    ),

    KnowledgeItem(
        name="Jetson",
        importance=65,
        category="Product",
        impact="MEDIUM",
        reason=(
            "Edge AI computing platform used in robotics, automation "
            "and embedded AI applications."
        ),
        tags=[
            "Edge AI",
            "Robotics",
            "Embedded"
        ]
    ),

    KnowledgeItem(
        name="BlueField",
        importance=75,
        category="Product",
        impact="HIGH",
        reason=(
            "Data Processing Unit (DPU) improving networking, security "
            "and datacenter performance."
        ),
        tags=[
            "DPU",
            "Networking",
            "Datacenter"
        ]
    ),

    KnowledgeItem(
        name="TensorRT",
        importance=80,
        category="Technology",
        impact="HIGH",
        reason=(
            "Inference optimization framework widely used for deploying "
            "AI models on NVIDIA hardware."
        ),
        tags=[
            "Inference",
            "Software",
            "AI"
        ]
    ),

    KnowledgeItem(
        name="Omniverse",
        importance=70,
        category="Product",
        impact="MEDIUM",
        reason=(
            "Platform for industrial digital twins, simulation and "
            "3D collaboration."
        ),
        tags=[
            "Simulation",
            "Digital Twin",
            "3D"
        ]
    )
]

        self.suppliers = [

    KnowledgeItem(
        name="TSMC",
        importance=100,
        aliases=[
            "Taiwan Semiconductor",
            "TSMC Co."
        ],
        category="Supplier",
        impact="CRITICAL",
        reason=(
            "NVIDIA's primary manufacturing partner for advanced AI GPUs. "
            "TSMC produces Blackwell and Hopper chips using cutting-edge "
            "process nodes. News about TSMC capacity, production delays, "
            "CoWoS packaging or advanced manufacturing can directly affect "
            "NVIDIA's revenue, margins and ability to meet AI demand."
        ),
        tags=[
            "Foundry",
            "Manufacturing",
            "CoWoS",
            "Blackwell",
            "Hopper",
            "AI GPU"
        ]
    ),

    KnowledgeItem(
        name="SK Hynix",
        importance=95,
        aliases=[
            "SKHynix"
        ],
        category="Supplier",
        impact="CRITICAL",
        reason=(
            "Leading supplier of High Bandwidth Memory (HBM) used in "
            "NVIDIA AI accelerators. HBM availability is one of the "
            "largest bottlenecks for AI GPU production."
        ),
        tags=[
            "HBM",
            "Memory",
            "AI",
            "Blackwell",
            "Hopper"
        ]
    ),

    KnowledgeItem(
        name="Micron",
        importance=80,
        category="Supplier",
        impact="HIGH",
        reason=(
            "Supplier of advanced memory solutions including HBM. "
            "Production expansion or supply constraints can influence "
            "NVIDIA's AI hardware production capacity."
        ),
        tags=[
            "HBM",
            "Memory",
            "DRAM"
        ]
    ),

    KnowledgeItem(
        name="Samsung",
        importance=75,
        aliases=[
            "Samsung Electronics"
        ],
        category="Supplier",
        impact="HIGH",
        reason=(
            "Potential supplier of advanced HBM memory and semiconductor "
            "technology supporting AI accelerator production."
        ),
        tags=[
            "HBM",
            "Memory",
            "Semiconductors"
        ]
    ),

    KnowledgeItem(
        name="ASE",
        importance=60,
        aliases=[
            "Advanced Semiconductor Engineering"
        ],
        category="Supplier",
        impact="MEDIUM",
        reason=(
            "Provides semiconductor packaging and testing services used "
            "within advanced chip manufacturing."
        ),
        tags=[
            "Packaging",
            "Testing"
        ]
    ),

    KnowledgeItem(
        name="Amkor",
        importance=55,
        category="Supplier",
        impact="MEDIUM",
        reason=(
            "Advanced semiconductor packaging partner supporting AI chip production."
        ),
        tags=[
            "Packaging",
            "Semiconductor"
        ]
    )

]
        self.customers = [

    KnowledgeItem(
        name="Microsoft",
        importance=100,
        aliases=[
            "Azure",
            "Azure AI"
        ],
        category="Customer",
        impact="CRITICAL",
        reason=(
            "Microsoft is one of NVIDIA's largest AI infrastructure customers. "
            "Azure AI invests billions of dollars into GPU clusters. "
            "Changes in Microsoft's AI CapEx are one of the strongest "
            "leading indicators of future NVIDIA revenue."
        ),
        tags=[
            "Azure",
            "Cloud",
            "AI",
            "GPU",
            "Datacenter"
        ]
    ),

    KnowledgeItem(
        name="Amazon",
        importance=95,
        aliases=[
            "AWS",
            "Amazon Web Services"
        ],
        category="Customer",
        impact="CRITICAL",
        reason=(
            "AWS is one of the world's largest cloud providers and a major "
            "buyer of NVIDIA AI GPUs. Expansion of AWS AI infrastructure "
            "usually increases NVIDIA GPU demand."
        ),
        tags=[
            "AWS",
            "Cloud",
            "AI",
            "GPU"
        ]
    ),

    KnowledgeItem(
        name="Google",
        importance=95,
        aliases=[
            "Google Cloud",
            "GCP",
            "Alphabet"
        ],
        category="Customer",
        impact="CRITICAL",
        reason=(
            "Google deploys NVIDIA GPUs across its cloud AI platform. "
            "Higher AI investment from Google generally supports "
            "future NVIDIA revenue growth."
        ),
        tags=[
            "Cloud",
            "AI",
            "GCP",
            "GPU"
        ]
    ),

    KnowledgeItem(
        name="Meta",
        importance=95,
        aliases=[
            "Facebook",
            "Meta Platforms"
        ],
        category="Customer",
        impact="CRITICAL",
        reason=(
            "Meta is one of NVIDIA's largest AI infrastructure customers "
            "and spends tens of billions on AI datacenters."
        ),
        tags=[
            "LLM",
            "AI",
            "GPU",
            "Datacenter"
        ]
    ),

    KnowledgeItem(
        name="Oracle",
        importance=90,
        aliases=[
            "Oracle Cloud",
            "OCI"
        ],
        category="Customer",
        impact="HIGH",
        reason=(
            "Oracle Cloud is rapidly expanding AI datacenters using "
            "NVIDIA GPUs. New Oracle AI infrastructure projects usually "
            "increase future GPU demand."
        ),
        tags=[
            "Cloud",
            "OCI",
            "AI"
        ]
    ),

    KnowledgeItem(
        name="Tesla",
        importance=75,
        category="Customer",
        impact="HIGH",
        reason=(
            "Tesla purchases NVIDIA hardware for AI development and "
            "high-performance computing."
        ),
        tags=[
            "Automotive",
            "AI",
            "Training"
        ]
    ),

    KnowledgeItem(
        name="Dell",
        importance=70,
        aliases=[
            "Dell Technologies"
        ],
        category="Customer",
        impact="MEDIUM",
        reason=(
            "Dell integrates NVIDIA AI infrastructure into enterprise "
            "server platforms."
        ),
        tags=[
            "Servers",
            "Enterprise",
            "AI"
        ]
    ),

    KnowledgeItem(
        name="Supermicro",
        importance=80,
        aliases=[
            "SMCI"
        ],
        category="Customer",
        impact="HIGH",
        reason=(
            "Major builder of AI servers powered by NVIDIA GPUs. "
            "Strong Supermicro demand often reflects healthy AI "
            "infrastructure spending."
        ),
        tags=[
            "Servers",
            "AI",
            "GPU"
        ]
    )

]

        self.partners = [

    KnowledgeItem(
        name="OpenAI",
        importance=100,
        aliases=[
            "ChatGPT"
        ],
        category="Partner",
        impact="CRITICAL",
        reason=(
            "One of the largest consumers of NVIDIA AI GPUs. "
            "Growth in OpenAI infrastructure, model training or inference "
            "directly increases demand for NVIDIA hardware."
        ),
        tags=[
            "LLM",
            "AI",
            "GPU",
            "Training",
            "Inference"
        ]
    ),

    KnowledgeItem(
        name="CoreWeave",
        importance=95,
        category="Partner",
        impact="CRITICAL",
        reason=(
            "Cloud infrastructure provider built almost entirely on "
            "NVIDIA GPUs. Expansion of CoreWeave usually signals "
            "strong future GPU demand."
        ),
        tags=[
            "Cloud",
            "GPU",
            "AI",
            "Datacenter"
        ]
    ),

    KnowledgeItem(
        name="xAI",
        importance=90,
        category="Partner",
        impact="HIGH",
        reason=(
            "Elon Musk's AI company building large GPU clusters for "
            "training frontier AI models."
        ),
        tags=[
            "LLM",
            "AI",
            "Training"
        ]
    ),

    KnowledgeItem(
        name="Anthropic",
        importance=90,
        category="Partner",
        impact="HIGH",
        reason=(
            "Leading AI company requiring large-scale GPU infrastructure "
            "for training and inference."
        ),
        tags=[
            "Claude",
            "LLM",
            "AI"
        ]
    ),

    KnowledgeItem(
        name="Cohere",
        importance=75,
        category="Partner",
        impact="MEDIUM",
        reason=(
            "Enterprise AI company using NVIDIA infrastructure."
        ),
        tags=[
            "Enterprise AI",
            "LLM"
        ]
    ),

    KnowledgeItem(
        name="Mistral AI",
        importance=75,
        category="Partner",
        impact="MEDIUM",
        reason=(
            "European frontier AI company developing large language models "
            "on NVIDIA hardware."
        ),
        tags=[
            "LLM",
            "Europe",
            "AI"
        ]
    )

]

        self.competitors = [

    KnowledgeItem(
        name="AMD",
        importance=100,
        aliases=[
            "Advanced Micro Devices",
            "MI300",
            "MI350"
        ],
        category="Competitor",
        impact="CRITICAL",
        reason=(
            "NVIDIA's primary competitor in AI accelerators. Product launches, "
            "pricing, benchmarks, customer wins or production issues can "
            "materially affect NVIDIA's market share and long-term valuation."
        ),
        tags=[
            "AI",
            "GPU",
            "Datacenter",
            "MI300",
            "Instinct"
        ]
    ),

    KnowledgeItem(
        name="Intel",
        importance=85,
        aliases=[
            "Gaudi",
            "Intel Foundry"
        ],
        category="Competitor",
        impact="HIGH",
        reason=(
            "Competes in AI accelerators, CPUs and datacenter infrastructure. "
            "Intel's AI strategy or cancellation of projects can change the "
            "competitive landscape."
        ),
        tags=[
            "Gaudi",
            "CPU",
            "AI",
            "Datacenter"
        ]
    ),

    KnowledgeItem(
        name="Broadcom",
        importance=80,
        aliases=[
            "AVGO"
        ],
        category="Competitor",
        impact="HIGH",
        reason=(
            "Designs custom AI accelerators and networking chips for large "
            "cloud providers. Growth in custom silicon may reduce future "
            "GPU demand."
        ),
        tags=[
            "ASIC",
            "Networking",
            "AI"
        ]
    ),

    KnowledgeItem(
        name="Marvell",
        importance=70,
        aliases=[
            "MRVL"
        ],
        category="Competitor",
        impact="MEDIUM",
        reason=(
            "Provides networking and custom AI silicon used by hyperscalers."
        ),
        tags=[
            "Networking",
            "ASIC"
        ]
    ),

    KnowledgeItem(
        name="Qualcomm",
        importance=60,
        aliases=[
            "QCOM"
        ],
        category="Competitor",
        impact="MEDIUM",
        reason=(
            "Develops AI processors for edge computing, PCs and mobile devices."
        ),
        tags=[
            "Edge AI",
            "Mobile",
            "PC"
        ]
    ),

    KnowledgeItem(
        name="Cerebras",
        importance=70,
        category="Competitor",
        impact="MEDIUM",
        reason=(
            "Developer of wafer-scale AI accelerators competing in high-end AI training."
        ),
        tags=[
            "AI",
            "Training"
        ]
    ),

    KnowledgeItem(
        name="Groq",
        importance=70,
        category="Competitor",
        impact="MEDIUM",
        reason=(
            "Builds inference accelerators competing with NVIDIA in low-latency AI."
        ),
        tags=[
            "Inference",
            "AI"
        ]
    )

]

        self.technologies = [

    KnowledgeItem(
        name="CUDA",
        importance=100,
        category="Technology",
        impact="CRITICAL",
        reason=(
            "NVIDIA's proprietary software platform. CUDA is one of the "
            "company's strongest competitive advantages and creates a large "
            "ecosystem of AI developers."
        ),
        tags=[
            "Software",
            "AI",
            "Platform",
            "Developer Ecosystem"
        ]
    ),

    KnowledgeItem(
        name="HBM",
        importance=100,
        aliases=[
            "High Bandwidth Memory"
        ],
        category="Technology",
        impact="CRITICAL",
        reason=(
            "HBM is essential for modern AI accelerators. Supply shortages "
            "or production expansion directly affect NVIDIA's ability to "
            "ship AI GPUs."
        ),
        tags=[
            "Memory",
            "AI",
            "GPU",
            "Datacenter"
        ]
    ),

    KnowledgeItem(
        name="CoWoS",
        importance=100,
        aliases=[
            "Chip on Wafer on Substrate"
        ],
        category="Technology",
        impact="CRITICAL",
        reason=(
            "Advanced packaging technology used by TSMC. CoWoS capacity is "
            "one of the biggest production constraints for NVIDIA AI GPUs."
        ),
        tags=[
            "Packaging",
            "TSMC",
            "Manufacturing"
        ]
    ),

    KnowledgeItem(
        name="NVLink",
        importance=95,
        category="Technology",
        impact="CRITICAL",
        reason=(
            "High-speed GPU interconnect enabling massive AI clusters."
        ),
        tags=[
            "Networking",
            "GPU",
            "AI"
        ]
    ),

    KnowledgeItem(
        name="NVSwitch",
        importance=90,
        category="Technology",
        impact="HIGH",
        reason=(
            "Switching technology connecting many GPUs together in AI systems."
        ),
        tags=[
            "Networking",
            "Datacenter"
        ]
    ),

    KnowledgeItem(
        name="TensorRT",
        importance=90,
        category="Technology",
        impact="HIGH",
        reason=(
            "Inference optimization software used to deploy AI models on NVIDIA hardware."
        ),
        tags=[
            "Inference",
            "Software"
        ]
    ),

    KnowledgeItem(
        name="Inference",
        importance=90,
        category="Technology",
        impact="HIGH",
        reason=(
            "Fastest-growing AI workload driving long-term GPU demand."
        ),
        tags=[
            "LLM",
            "AI"
        ]
    ),

    KnowledgeItem(
        name="Training",
        importance=90,
        category="Technology",
        impact="HIGH",
        reason=(
            "Training of frontier AI models remains one of NVIDIA's largest "
            "sources of GPU demand."
        ),
        tags=[
            "LLM",
            "GPU",
            "AI"
        ]
    ),

    KnowledgeItem(
        name="InfiniBand",
        importance=85,
        category="Technology",
        impact="HIGH",
        reason=(
            "High-performance networking technology used to build large AI clusters."
        ),
        tags=[
            "Networking",
            "Datacenter"
        ]
    ),

    KnowledgeItem(
        name="Spectrum-X",
        importance=80,
        category="Technology",
        impact="HIGH",
        reason=(
            "Ethernet networking platform optimized for AI infrastructure."
        ),
        tags=[
            "Ethernet",
            "AI",
            "Networking"
        ]
    )

]

        self.catalysts = [

    KnowledgeItem(
        name="Earnings",
        importance=100,
        category="Catalyst",
        impact="CRITICAL",
        reason=(
            "Quarterly earnings are the single most important recurring "
            "event for NVIDIA. Revenue growth, margins and AI demand "
            "can significantly change valuation."
        ),
        tags=[
            "Quarterly Results",
            "Revenue",
            "EPS"
        ]
    ),

    KnowledgeItem(
        name="Guidance",
        importance=100,
        category="Catalyst",
        impact="CRITICAL",
        reason=(
            "Forward guidance often has a larger impact on the stock than "
            "historical earnings because it reflects future demand."
        ),
        tags=[
            "Forecast",
            "Revenue",
            "Growth"
        ]
    ),

    KnowledgeItem(
        name="AI Infrastructure",
        importance=100,
        category="Catalyst",
        impact="CRITICAL",
        reason=(
            "Global investment in AI infrastructure is the primary long-term "
            "driver of NVIDIA's datacenter business."
        ),
        tags=[
            "Datacenter",
            "Cloud",
            "AI"
        ]
    ),

    KnowledgeItem(
        name="AI CapEx",
        importance=95,
        category="Catalyst",
        impact="CRITICAL",
        reason=(
            "Capital expenditure by hyperscalers is one of the strongest "
            "leading indicators of future GPU demand."
        ),
        tags=[
            "Microsoft",
            "Amazon",
            "Google",
            "Meta"
        ]
    ),

    KnowledgeItem(
        name="GPU Demand",
        importance=95,
        category="Catalyst",
        impact="CRITICAL",
        reason=(
            "Changes in AI GPU demand directly influence NVIDIA's revenue "
            "growth and production plans."
        ),
        tags=[
            "Datacenter",
            "AI",
            "GPU"
        ]
    ),

    KnowledgeItem(
        name="Export Restrictions",
        importance=95,
        category="Catalyst",
        impact="CRITICAL",
        reason=(
            "US export restrictions on advanced AI chips can materially "
            "reduce NVIDIA's addressable market and revenue."
        ),
        tags=[
            "China",
            "Regulation",
            "Government"
        ]
    ),

    KnowledgeItem(
        name="Supply Chain",
        importance=90,
        category="Catalyst",
        impact="HIGH",
        reason=(
            "Supply chain bottlenecks affecting TSMC, HBM memory or advanced "
            "packaging can limit NVIDIA's shipments."
        ),
        tags=[
            "TSMC",
            "HBM",
            "CoWoS"
        ]
    ),

    KnowledgeItem(
        name="Product Launch",
        importance=90,
        category="Catalyst",
        impact="HIGH",
        reason=(
            "Major product launches such as Blackwell or Rubin influence "
            "future demand and long-term valuation."
        ),
        tags=[
            "Blackwell",
            "Rubin",
            "Roadmap"
        ]
    ),

    KnowledgeItem(
        name="Hyperscaler Spending",
        importance=90,
        category="Catalyst",
        impact="HIGH",
        reason=(
            "Investment announcements from Microsoft, Amazon, Google, "
            "Meta or Oracle usually precede higher NVIDIA GPU demand."
        ),
        tags=[
            "Cloud",
            "AI",
            "CapEx"
        ]
    ),

    KnowledgeItem(
        name="Large GPU Orders",
        importance=90,
        category="Catalyst",
        impact="HIGH",
        reason=(
            "Large GPU purchase announcements from AI companies often "
            "translate directly into future revenue."
        ),
        tags=[
            "OpenAI",
            "CoreWeave",
            "xAI"
        ]
    )

]