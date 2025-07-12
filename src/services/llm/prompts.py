from typing import Dict, List
#  this takes a list of metadata of papers
# and ask with prmpt to generte a LR


def get_lit_review_prompt(papers: List[Dict]) -> str:
    bullet_points = []
    for paper in papers:
        summary = paper.get("chunk", "")[:500]
        bullet = (
            f"• **Title:** {paper.get('title', 'N/A')} ({paper.get('year', 'N/A')})\n"
            f"  - Authors: {paper.get('authors', 'N/A')}\n"
            f"  - Method: {paper.get('method', 'N/A')}\n"
            f"  - Source: {paper.get('source', 'arXiv')}\n"
            f"  - Summary: {summary}\n"
        )
        bullet_points.append(bullet)
    context = "\n".join(bullet_points)
    return f"""You are an academic writing assistant.
Given the following extracted information from multiple scientific papers, 
generate a concise **literature review** on the topic.
Each entry includes title, authors, year, 
and a short chunk of content from the paper.
Summarize the key themes, compare methods, and synthesize the findings.
Context:
{context}
Literature Review:
"""
