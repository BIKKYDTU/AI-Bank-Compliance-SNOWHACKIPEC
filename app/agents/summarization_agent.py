import re


class SummarizationAgent:
    def summarize(self, text: str) -> dict:
        if not text:
            return {"obligations": [], "deadlines": [], "summary_text": ""}

        cleaned = " ".join(text.split())
        sentences = re.split(r"(?<=[.!?])\s+", cleaned)

        obligation_re = re.compile(
            r"\b(must|shall|required to|is required to|should|need to)\b",
            re.IGNORECASE,
        )
        obligations = [s.strip() for s in sentences if obligation_re.search(s)]

        if not obligations:
            obligations = [s.strip() for s in sentences if s.strip()][:3]

        date_re = re.compile(
            r"\b(?:jan|feb|mar|apr|may|jun|jul|aug|sep|sept|oct|nov|dec)[a-z]*\b",
            re.IGNORECASE,
        )
        deadline_kw_re = re.compile(
            r"\b(by|within|no later than|on or before|before|after)\b",
            re.IGNORECASE,
        )
        deadlines = []
        for s in sentences:
            if deadline_kw_re.search(s) or date_re.search(s):
                deadlines.append(s.strip())

        summary_text = " ".join([s.strip() for s in sentences if s.strip()][:3])

        return {
            "obligations": obligations[:10],
            "deadlines": deadlines[:10],
            "summary_text": summary_text,
        }
