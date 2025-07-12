from src.services.scraping import arxiv_scraper as arx


#  mock the _fetch_feed function to avoid network calls
def test_arxiv_search_returns_papers(monkeypatch):
    # Patch _fetch_feed so we don't hit the network
    sample_xml = """<?xml version="1.0"?>
    <feed xmlns="http://www.w3.org/2005/Atom">
      <entry>
        <id>http://arxiv.org/abs/1234.5678v1</id>
        <updated>2024-01-01T00:00:00Z</updated>
        <published>2024-01-01T00:00:00Z</published>
        <title>Example Title</title>
        <summary>Short abstract.</summary>
        <author><name>Jane Doe</name></author>
        <category term="cs.AI"/>
        <link href="http://arxiv.org/pdf/1234.5678v1" type="application/pdf"/>
      </entry>
    </feed>"""
    monkeypatch.setattr(arx, "_fetch_feed", lambda _: sample_xml)

    papers = arx.arxiv_search("example", max_results=1)
    assert len(papers) == 1
    assert papers[0].title == "Example Title"
