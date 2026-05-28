def create_chunks(text, chunk_size=200):

    chunks = []

    for i in range(0, len(text), chunk_size):

        chunk = text[i:i + chunk_size]

        chunks.append(chunk)

    return chunks


def attach_metadata(chunks, company="Unknown", section="general"):

    metadata_chunks = []

    for chunk in chunks:

        metadata_chunks.append({
            "text": chunk,
            "company": company,
            "section": section
        })

    return metadata_chunks