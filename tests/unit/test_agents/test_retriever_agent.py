from src.agents.retriever_agent import RetrieverAgent


def test_retriever_agent():

    # somes paper text
    chunks = ["Transformers were introduced in 2017 by Vaswani et al."]
    metadatas = [{"title": "Attention is All You Need", "year": 2017}]

    # 1. Embed +Index
    retriever = RetrieverAgent(dim=1024)
    retriever.index(chunks, metadatas)

    # 2. Query
    results = retriever.retrieve("what are transformers?")
    for i, res in enumerate(results):
        print(f"\nResult {i+1}:\n{res}")
