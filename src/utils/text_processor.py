import re


def clean_text(text: str) -> str:
    """
    Clean and normalize text by removing unwanted characters and formatting
    """
    if not text:
        return ""
    text = re.sub(r"[^\w\s\.\,\;\:\!\?\-\(\)]", " ", text)
    text = re.sub(r"[.]{2,}", ".", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()
