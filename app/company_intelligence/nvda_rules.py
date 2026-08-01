class NvidiaRules:

    @staticmethod
    def get_rules():

        return [

            {
                "name": "Blackwell Production",
                "requires": [
                    "Blackwell",
                    "TSMC"
                ],
                "bonus": 100
            },

            {
                "name": "HBM Supply",
                "requires": [
                    "HBM",
                    "SK Hynix"
                ],
                "bonus": 80
            },

            {
                "name": "AI Infrastructure Demand",
                "requires": [
                    "Microsoft",
                    "AI Infrastructure"
                ],
                "bonus": 80
            },

            {
                "name": "OpenAI GPU Demand",
                "requires": [
                    "OpenAI",
                    "GPU Demand"
                ],
                "bonus": 80
            },

            {
                "name": "Export Restrictions",
                "requires": [
                    "Export Restrictions",
                    "China"
                ],
                "bonus": 120
            },

            {
                "name": "Strong Earnings",
                "requires": [
                    "Earnings",
                    "Guidance"
                ],
                "bonus": 150
            },

            {
                "name": "AMD Delay",
                "requires": [
                    "AMD",
                    "Delay"
                ],
                "bonus": 50
            },

            {
                "name": "Intel AI Exit",
                "requires": [
                    "Intel",
                    "Cancel"
                ],
                "bonus": 50
            }

        ]