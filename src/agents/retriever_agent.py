from typing import Dict, List

from src.services.rag.embedder import Embedder
from src.services.rag.vector_store import PineconeVectorStore


class RetrieverAgent:
    def __init__(self, dim: int = 1024):
        self.embedder = Embedder()
        self.vector_store = PineconeVectorStore(dim)

    def index(self, chunks: List[str], metadatas: List[Dict]):
        embeddings = self.embedder.embed_texts(chunks)
        self.vector_store.add(embeddings, metadatas)

    def retrieve(self, query: str, k: int = 5):
        query_emb = self.embedder.embed_texts([query])[0]
        return self.vector_store.search(query_emb, top_k=k)
