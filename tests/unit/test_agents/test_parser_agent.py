from datetime import datetime

from src.agents.parser_agent import ParserAgent
from src.models.paper import Paper


def fake_extract(_url: str) -> str:
    return "Lorem ipsum dolor sit amet."


def test_parser_agent(monkeypatch):
    # Patch the real PDF download to avoid network
    from src.agents import parser_agent as agent_mod

    monkeypatch.setattr(agent_mod, "extract_pdf_text", fake_extract)

    paper = Paper(
        arxiv_id="1234.5678",
        title="Dummy",
        summary="x",
        published=datetime.now(),
        authors=["A"],
        categories=[],
        pdf_url="http://example.com/dummy.pdf",
    )

    parsed = ParserAgent().parse([paper])[0]
    assert parsed.full_text.startswith("Lorem ipsum")
