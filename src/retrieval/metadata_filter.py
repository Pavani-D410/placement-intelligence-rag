def filter_by_metadata(chunks, company=None, section=None):

    filtered_chunks = []

    for chunk in chunks:

        if company and chunk["company"] != company:
            continue

        if section and chunk["section"] != section:
            continue

        filtered_chunks.append(chunk)

    return filtered_chunks