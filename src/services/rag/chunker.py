import os
from typing import List

from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.models.paper import Paper

CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 1000))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 200))


def split_text(text: str) -> List[str]:
    """
    Clean and chunk a single text string using LangChain.
    Returns a list of text chunks.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n\n", "\n", ".", " "],
    )
    return splitter.split_text(text)


def chunk_paper(paper: Paper) -> List[str]:
    """
    Splits the paper's full_text into overlapping chunks.
    """
    if not paper.full_text:
        return []

    chunks = split_text(paper.full_text)
    return chunks
