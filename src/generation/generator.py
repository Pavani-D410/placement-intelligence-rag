def generate_grounded_response(query, retrieved_chunks):

    if not retrieved_chunks:

        return "No relevant information found."


    response = "Based on retrieved documents:\n\n"

    for chunk in retrieved_chunks:

        response += f"- {chunk['text']}\n"

    return response