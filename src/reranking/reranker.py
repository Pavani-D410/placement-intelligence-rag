def rerank_documents(query, documents):

    ranked_results = []

    query_words = set(
        query.lower().split()
    )

    for doc in documents:

        doc_words = set(
            doc.lower().split()
        )

        score = len(
            query_words.intersection(doc_words)
        )

        ranked_results.append(
            (doc, score)
        )

    ranked_results = sorted(
        ranked_results,
        key=lambda x: x[1],
        reverse=True
    )

    return ranked_results