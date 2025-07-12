from typing import List
from src.core import log
from src.models.paper import Paper
from src.services.scraping import arxiv_scraper


class ScraperAgent:
    """
    High-level agent that wraps scraping logic from arXiv 
    """

    def __init__(self, max_results: int = 10):
        self.max_results = max_results

    def run(self, query: str) -> List[Paper]:
        log.info(f"[scraper] Searching arXiv for: '{query}'")
        try:
            papers = arxiv_scraper.search(query, max_results=self.max_results)
            log.info(f"[scraper] Found {len(papers)} papers.")
            return papers
        except Exception as e:
            log.error(f"[scraper] Failed to scrape: {e}")
            return []
