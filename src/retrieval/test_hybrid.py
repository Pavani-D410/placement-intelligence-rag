from src.retrieval.hybrid_search import HybridRetriever


documents = [
    "Amazon offers 28.6 LPA package",
    "Google offers 42.0 LPA package",
    "Microsoft focuses on OS and DBMS"
]


retriever = HybridRetriever(documents)

results = retriever.keyword_search(
    "highest package company"
)

print(results)