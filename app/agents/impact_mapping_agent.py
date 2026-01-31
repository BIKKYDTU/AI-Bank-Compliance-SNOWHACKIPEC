class ImpactMappingAgent:
    def map_impacts(self, summary: dict) -> dict:
        text_parts = []
        for key in ("summary_text", "obligations", "deadlines"):
            value = summary.get(key, "")
            if isinstance(value, list):
                text_parts.extend(value)
            elif isinstance(value, str):
                text_parts.append(value)

        combined = " ".join(text_parts).lower()

        department_keywords = {
            "Compliance": ["compliance", "regulatory", "rbi", "fema"],
            "Risk": ["risk", "capital", "liquidity", "exposure"],
            "Treasury": ["treasury", "fx", "foreign exchange"],
            "Operations": ["operations", "settlement", "clearing"],
            "Legal": ["legal", "law", "statute"],
            "IT": ["it", "technology", "systems", "cyber"],
            "Retail Banking": ["retail", "branch", "customer"],
            "Corporate Banking": ["corporate", "wholesale"],
        }

        product_keywords = {
            "Accounts": ["account", "deposit", "savings", "current account"],
            "Loans": ["loan", "credit", "lending"],
            "Cards": ["card", "debit", "credit card"],
            "Payments": ["payment", "transfer", "upi", "neft", "rtgs"],
            "Remittance/Forex": ["remittance", "forex", "foreign exchange", "fx"],
            "KYC/Onboarding": ["kyc", "onboarding", "customer due diligence"],
        }

        departments = [
            name
            for name, keywords in department_keywords.items()
            if any(k in combined for k in keywords)
        ]
        products = [
            name
            for name, keywords in product_keywords.items()
            if any(k in combined for k in keywords)
        ]

        if not departments:
            departments = ["Compliance"]

        return {"departments": departments, "products": products}
