from src.agents.scraper_agent import ScraperAgent


def test_scraper_agent_live():
    agent = ScraperAgent(max_results=3)
    papers = agent.run("graph neural networks")
    assert len(papers) <= 3
    assert all(p.pdf_url for p in papers)
