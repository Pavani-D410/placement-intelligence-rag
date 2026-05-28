import chromadb


client = chromadb.Client()

collection = client.get_or_create_collection(
    name="placement_rag"
)


def store_embeddings(chunks, embeddings):

    for i, chunk in enumerate(chunks):

        collection.add(
            documents=[chunk["text"]],
            embeddings=[embeddings[i]],
            metadatas=[{
                "company": chunk["company"],
                "section": chunk["section"]
            }],
            ids=[str(i)]
        )


def search_embeddings(query_embedding, top_k=3):

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results