import re


class ValidationAgent:
    def validate(self, summary: dict, retrieved_docs: list) -> dict:
        obligations = summary.get("obligations", [])
        evidence = []

        if not retrieved_docs or not obligations:
            return {"validation_status": "insufficient_data", "evidence": []}

        for obligation in obligations[:5]:
            doc = retrieved_docs[0]
            content = doc.page_content or ""
            page_match = re.search(r"--- Page (\d+) ---", content)
            page_num = page_match.group(1) if page_match else "N/A"
            snippet = content[:300].strip().replace("\n", " ")
            evidence.append(
                {
                    "obligation": obligation,
                    "evidence_snippets": [
                        {
                            "text": snippet,
                            "page": page_num,
                        }
                    ],
                }
            )

        status = "verified" if evidence else "needs_review"
        return {"validation_status": status, "evidence": evidence}
