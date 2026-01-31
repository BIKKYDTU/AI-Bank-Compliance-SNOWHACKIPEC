from pypdf import PdfReader
try:
    from langchain_core.documents import Document
except ImportError:
    from langchain.schema import Document
import io

class DocumentIngestionService:
    def __init__(self, vector_store):
        self.vector_store = vector_store

    def ingest_pdf(self, file_bytes, filename, document_id, doc_type="regulatory_pdf"):
        pdf_file = io.BytesIO(file_bytes)
        reader = PdfReader(pdf_file)
        text = ""
        for i, page in enumerate(reader.pages):
            text += f"--- Page {i+1} ---\n{page.extract_text()}\n"
        
        doc = Document(page_content=text, metadata={"source": filename, "document_id": document_id, "type": doc_type})
        self.vector_store.add_documents([doc])
        return {"success": True, "page_count": len(reader.pages)}