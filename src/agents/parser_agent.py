from typing import List

from src.core import exceptions, log
from src.models import Paper
from src.utils import extract_pdf_text


class ParserAgent:
    def __init__(self, batch_size: int = 3):
        self.batch_size = batch_size

    def _parse_one(self, paper: Paper) -> Paper:
        if paper.pdf_url is None:
            log.warning(f"Paper {paper.id} has no PDF URL, skipping parsing.")
            return paper

        try:
            text = extract_pdf_text(paper.pdf_url)
            paper.full_text = text.strip()  # put it in Paper model
            log.info(f"[parser] parsed {paper.arxiv_id} ({len(text)} chars)")
            return paper

        except exceptions.AppError as e:
            log.error(f"[parser] failed {paper.arxiv_id}: {e}")
            return paper

    def parse(
        self, papers: List[Paper]
    ) -> List[Paper]:  # papers will be delivered from arxiv_srapper
        """parse pdf in batches"""
        parsed: List[Paper] = []
        for i in range(0, len(papers), self.batch_size):
            batch = papers[i:i + self.batch_size]
            parsed.extend(self._parse_one(p) for p in batch)
        return parsed
