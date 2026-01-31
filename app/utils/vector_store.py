import chromadb
from chromadb.config import Settings
try:
    from langchain_text_splitters import RecursiveCharacterTextSplitter
except ImportError:
    from langchain.text_splitter import RecursiveCharacterTextSplitter
try:
    from langchain_community.embeddings import HuggingFaceEmbeddings
except ImportError:
    from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from typing import List, Optional, Dict, Any
import os
from app.config import EMBEDDING_MODEL, CHROMA_PERSIST_DIR, CHUNK_SIZE, CHUNK_OVERLAP, TOP_K_RESULTS

class VectorStore:
    def __init__(self):
        abs_persist_path = os.path.abspath(CHROMA_PERSIST_DIR)
        os.makedirs(abs_persist_path, exist_ok=True)
        self.embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
        
        # Fixed initialization for newer ChromaDB
        client_settings = Settings(is_persistent=True, persist_directory=abs_persist_path, anonymized_telemetry=False)
        chroma_client = chromadb.PersistentClient(path=abs_persist_path, settings=client_settings)
        self.vectorstore = Chroma(client=chroma_client, collection_name="bankguard_docs", embedding_function=self.embeddings)

    def add_documents(self, documents):
        chunks = self.text_splitter.split_documents(documents)
        return self.vectorstore.add_documents(chunks)

    def search(self, query, k=TOP_K_RESULTS, where=None):
        return self.vectorstore.similarity_search(query, k=k, filter=where)