import os
from typing import Dict, List

from pinecone import Pinecone, ServerlessSpec

from src.core import log

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENV = os.getenv("PINECONE_ENV", "us-east-1")
INDEX_NAME = os.getenv("PINECONE_INDEX", "literature-index")


class PineconeVectorStore:
    def __init__(self, dim: int):
        # Initialize Pinecone client
        self.pc = Pinecone(api_key=PINECONE_API_KEY)

        # Create index if it doesn't exist
        if INDEX_NAME not in self.pc.list_indexes().names():
            self.pc.create_index(
                name=INDEX_NAME,
                dimension=dim,
                metric="cosine",
                spec=ServerlessSpec(cloud="aws", region="us-east-1"),
            )

        # Connect to the index
        self.index = self.pc.Index(INDEX_NAME)
        log.info(f"[pinecone] Connected to index '{INDEX_NAME}'")

    def add(self, embeddings: List[List[float]], metadatas: List[Dict]):
        vectors = [
            (str(i), emb, meta)
            for i, (emb, meta) in enumerate(zip(embeddings, metadatas))
        ]
        self.index.upsert(vectors=vectors)
        log.info(f"[pinecone] Upserted {len(vectors)} vectors")

    def search(self, query_embedding: List[float], top_k: int = 5):
        results = self.index.query(
            vector=query_embedding, top_k=top_k, include_metadata=True
        )
        return [(match.metadata, match.score) for match in results.matches]
