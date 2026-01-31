"""
Optional RAG (Retrieval-Augmented) helpers.

RAG retrieval itself is done in orchestration.py via vector_store.search().
This module can hold extra helpers, e.g. query building or multi-query retrieval.
"""

from app.utils.vector_store import VectorStore


def search_context(
    query: str,
    k: int = 5,
    document_id: str | None = None,
    doc_type: str | None = "regulatory_pdf",
) -> list:
    """
    Retrieve relevant chunks from the vector store (RAG retrieval step).
    Used as an optional wrapper so orchestration or UI can call one place.
    """
    vs = VectorStore()
    where = None
    if document_id and doc_type:
        where = {"type": doc_type, "document_id": document_id}
    return vs.search(query, k=k, where=where)


def combined_text_from_docs(docs: list) -> str:
    """Join retrieved document contents into one string for agents."""
    return "\n".join(d.page_content for d in docs) if docs else ""
