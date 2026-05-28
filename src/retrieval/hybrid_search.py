from rank_bm25 import BM25Okapi
import numpy as np


class HybridRetriever:

    def __init__(self, documents):

        self.documents = documents

        tokenized_docs = [
            doc.lower().split()
            for doc in documents
        ]

        self.bm25 = BM25Okapi(tokenized_docs)

    def keyword_search(self, query, top_k=3):

        scores = self.bm25.get_scores(
            query.lower().split()
        )

        top_indices = np.argsort(scores)[::-1][:top_k]

        return [
            self.documents[i]
            for i in top_indices
        ]