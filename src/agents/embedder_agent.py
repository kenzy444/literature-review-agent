from typing import List

from src.core import log
from src.models.paper import Paper
from src.services.rag.chunker import chunk_paper
from src.services.rag.embedder import Embedder


class EmbedderAgent:
    def __init__(self):
        self.embedder = Embedder()

    def run(self, paper: Paper) -> List[dict]:
        """
        Chunks the full_text of the paper, embeds each chunk,
        and returns a list of {chunk, embedding} dicts.
        """
        log.info(f"[embedder-agent] Processing paper: {paper.title}")

        chunks = chunk_paper(paper)
        if not chunks:
            log.warning("[embedder-agent] No chunks found.")
            return []

        embeddings = self.embedder.embed_texts(chunks)
        log.info(f"[embedder-agent] Embedded {len(chunks)} chunks")

        # Link each chunk with its embedding
        chunk_embeddings = [
            {"chunk": chunk, "embedding": embedding}
            for chunk, embedding in zip(chunks, embeddings)
        ]

        return chunk_embeddings
