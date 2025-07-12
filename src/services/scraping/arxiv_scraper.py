from __future__ import annotations  #to not write type as str
import urllib.parse as _url
from datetime import datetime
from typing import List
import feedparser
import httpx
from src.core import exceptions, log
from src.models import Paper
_API_URL = "https://export.arxiv.org/api/query"


def _sanitize_query(q: str) -> str:
    """urlencode for arXiv syntax and strip"""
    return _url.quote_plus(q.strip())


def _build_url(query: str, start: int, max_results: int) -> str:
    params = {
        "search_query": f"all:{query}",
        "start": start,
        "max_results": max_results,
        "sortBy": "relevance",
    } 
    # format into valid url that includes evything
    return f"{_API_URL}?{_url.urlencode(params)}"


#  send GET request,get XMl
def _fetch_feed(url: str) -> str:
    try:
        resp = httpx.get(url, timeout=20)
        resp.raise_for_status()
        return resp.text
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            raise exceptions.NotFoundError("arXiv endpoint 404") from e
        raise exceptions.ExternalServiceError("arXiv", str(e)) from e
    except httpx.HTTPError as e:
        raise exceptions.ExternalServiceError("arXiv", str(e)) from e


#  metadata
def _parse_feed(xml: str) -> List[Paper]:
    parsed = feedparser.parse(xml)
    papers: List[Paper] = []
    for entry in parsed.entries:
        pdf_link = next(
            (line.href for line in entry.links 
             if line.type == "application/pdf"), None
        )
        papers.append(
            Paper(
                arxiv_id=entry.id.split("/")[-1],
                title=entry.title.strip(),
                summary=entry.summary.strip(),
                published=datetime(*entry.published_parsed[:6]),
                authors=[a.name for a in entry.authors],
                categories=[t["term"] for t in entry.tags],
                pdf_url=pdf_link,
            )
        )
    return papers


#  final func
def arxiv_search(query: str, 
                 max_results: int = 25) -> List[Paper]:
    if max_results <= 0:
        raise ValueError("max_results can't be <=0")
    log.info(f"[arXiv] searching for '{query}' (max={max_results})")
    url = _build_url(_sanitize_query(query), 
                     start=0, max_results=max_results)
    xml = _fetch_feed(url)
    papers = _parse_feed(xml)
    log.info(f"[arXiv] found {len(papers)} papers")
    return papers
