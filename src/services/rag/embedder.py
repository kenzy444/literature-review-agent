from typing import List

import numpy as np
from sentence_transformers import SentenceTransformer

from src.core import log


#  "mixedbread-ai/mxbai-embed-large-v1"
class Embedder:
    def __init__(self, model_name: str = "BAAI/bge-large-en-v1.5"):
        log.info(f"[embedder] Loading embedding model: {model_name}")
        self.model = SentenceTransformer(model_name)

    def embed_texts(self, texts: List[str]) -> np.ndarray:
        """
        Embed a list of text chunks and return a numpy array of vectors.
        """
        log.debug(f"[embedder] Embedding {len(texts)} chunks")
        return self.model.encode(
            texts,
            show_progress_bar=True,
            convert_to_numpy=True,
            normalize_embeddings=True,
        )
