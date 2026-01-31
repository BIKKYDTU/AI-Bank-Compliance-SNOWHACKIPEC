import uuid

from app.services.document_ingestion import DocumentIngestionService
from app.utils.vector_store import VectorStore
from app.agents.summarization_agent import SummarizationAgent
from app.agents.impact_mapping_agent import ImpactMappingAgent
from app.agents.validation_agent import ValidationAgent
from app.agents.action_planner_agent import ActionPlannerAgent


class OrchestrationService:
    def __init__(self):
        self.vector_store = VectorStore()
        self.ingestion = DocumentIngestionService(self.vector_store)
        self.summarizer = SummarizationAgent()
        self.impact_mapper = ImpactMappingAgent()
        self.validator = ValidationAgent()
        self.action_planner = ActionPlannerAgent()

    def process_pdf(
        self,
        file_bytes: bytes,
        filename: str,
        query: str | None = None,
        retrieval_mode: str = "both",
    ) -> dict:
        document_id = str(uuid.uuid4())

        # 1. Ingest PDF
        self.ingestion.ingest_pdf(
            file_bytes,
            filename,
            document_id,
            doc_type="regulatory_pdf",
        )

        # 2. Retrieve relevant context
        effective_query = (query or "foreign exchange drawal rules").strip()
        where = None
        if retrieval_mode == "regulatory_only":
            where = {"type": "regulatory_pdf", "document_id": document_id}
        elif retrieval_mode == "policy_only":
            where = {"type": "internal_policy"}
        retrieved_docs = self.vector_store.search(effective_query, k=5, where=where)

        combined_text = "\n".join(d.page_content for d in retrieved_docs)

        # 3. Summarize
        summary = self.summarizer.summarize(combined_text)

        # 4. Impact mapping
        impact = self.impact_mapper.map_impacts(summary)

        # 5. Validation
        validation = self.validator.validate(summary, retrieved_docs)

        # 6. Action planning
        action_plan = self.action_planner.generate_action_plan(
            summary,
            impact,
            validation,
        )

        # 7. Final output
        return {
            "document_id": document_id,
            "summary": summary,
            "impact": impact,
            "validation": validation,
            "action_plan": action_plan,
        }

    def add_internal_policy(self, file_bytes: bytes, filename: str) -> dict:
        document_id = str(uuid.uuid4())
        return self.ingestion.ingest_pdf(
            file_bytes,
            filename,
            document_id,
            doc_type="internal_policy",
        )

    def clear_database(self) -> None:
        self.vector_store.clear()
