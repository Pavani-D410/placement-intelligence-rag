def extract_sources(retrieved_chunks):

    sources = []

    for chunk in retrieved_chunks:

        company = chunk.get(
            "company",
            "Unknown"
        )

        section = chunk.get(
            "section",
            "general"
        )

        sources.append(
            f"{company} - {section}"
        )

    return list(set(sources))