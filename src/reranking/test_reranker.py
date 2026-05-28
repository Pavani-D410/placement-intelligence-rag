from src.reranking.reranker import (
    rerank_documents
)


query = "highest package company"


documents = [
    "Amazon offers 28.6 LPA package",
    "Google offers 42.0 LPA package",
    "Microsoft focuses on OS and DBMS"
]


results = rerank_documents(
    query,
    documents
)

print(results)