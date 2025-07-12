from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional


@dataclass
class Paper:
    arxiv_id: str
    title: str
    summary: str
    published: datetime
    authors: List[str]
    categories: List[str]
    pdf_url: Optional[str] = None
    full_text: Optional[str] = None
