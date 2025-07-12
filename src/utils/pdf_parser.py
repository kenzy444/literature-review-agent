from io import BytesIO  # treat bytes as file like obj

import httpx
from pdfminer.high_level import extract_text

from src.core import exceptions, log


def download_pdf(url: str) -> bytes:
    """fetch a pdf + return raw bytes"""
    try:
        response = httpx.get(url, timeout=20)
        if response.status_code == 404:
            raise exceptions.NotFoundError(f"PDF not found :{url}")

        response.raise_for_status()
        return response.content

    except httpx.HTTPError as e:
        raise exceptions.ExternalServiceError("PDF download : ", str(e)) from e


def bytes_to_text(pdf_bytes: bytes) -> str:
    """extracts texts from bytes"""
    with BytesIO(pdf_bytes) as bio:
        return extract_text(bio)


def extract_pdf_text(url: str) -> str:
    log.info(f"Extracting text from PDF at {url}")
    pdf_bytes = download_pdf(url)
    text = bytes_to_text(pdf_bytes)
    return text
