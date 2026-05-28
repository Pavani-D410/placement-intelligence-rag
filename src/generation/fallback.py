def fallback_response(retrieved_chunks):

    if not retrieved_chunks:

        return (
            "No relevant information found "
            "in the uploaded dataset."
        )

    return None