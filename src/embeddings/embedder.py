import ollama


def generate_embeddings(chunks):

    embeddings = []

    for chunk in chunks:

        response = ollama.embeddings(
            model="nomic-embed-text",
            prompt=chunk["text"]
        )

        embeddings.append(response["embedding"])

    return embeddings