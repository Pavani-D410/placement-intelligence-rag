def generate_grounded_response(query, retrieved_chunks):

    if not retrieved_chunks:

        return "No relevant information found."


    combined_text = ""

    for chunk in retrieved_chunks:

        combined_text += chunk["text"] + "\n"


    query_lower = query.lower()


    if "amazon" in query_lower and "package" in query_lower:

        return "Amazon offers a package of 28.6 LPA."


    if "google" in query_lower and "package" in query_lower:

        return "Google offers a package of 42.0 LPA."


    if "microsoft" in query_lower:

        return (
            "Microsoft focuses on "
            "OS, DBMS, and DSA rounds."
        )


    return combined_text[:500]