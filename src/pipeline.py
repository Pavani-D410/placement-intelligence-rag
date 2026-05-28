from src.ingestion.pdf_loader import load_pdf


from src.chunking.semantic_chunker import (
    create_chunks,
    attach_metadata
)

from src.embeddings.embedder import (
    generate_embeddings
)

from src.vectordb.chroma_store import (
    store_embeddings,
    search_embeddings
)

from src.generation.generator import (
    generate_grounded_response
)

from src.generation.citations import (
    extract_sources
)

from src.generation.fallback import (
    fallback_response
)


PLACEMENT_KEYWORDS = [

    "amazon",
    "google",
    "microsoft",
    "infosys",
    "tcs",
    "wipro",
    "package",
    "cgpa",
    "placement",
    "interview",
    "backlog",
    "salary",
    "company",
    "eligibility",
    "offer",
    "lpa",
    "job"
]


def is_placement_query(query):

    query_lower = query.lower()

    for keyword in PLACEMENT_KEYWORDS:

        if keyword in query_lower:

            return True

    return False


def run_pipeline(query):

    if not is_placement_query(query):

        return {
            "answer": (
                "No relevant information found "
                "in the uploaded dataset."
            ),
            "sources": []
        }

    pdf_path = (
        "data/raw/"
        "Placement_RAG_Dataset_Enhanced.pdf"
    )

    pdf_text = load_pdf(pdf_path)

    with open(
    "cache/ocr_text.txt",
    "r",
    encoding="utf-8"
     ) as file:

     ocr_text = file.read()

    text = pdf_text + "\n" + ocr_text

    chunks = create_chunks(
        text,
        chunk_size=200
    )

    metadata_chunks = attach_metadata(
        chunks,
        company="Placement Dataset",
        section="general"
    )

    embeddings = generate_embeddings(
        metadata_chunks
    )

    store_embeddings(
        metadata_chunks,
        embeddings
    )

    query_embedding = generate_embeddings([
        {
            "text": query
        }
    ])[0]

    results = search_embeddings(
        query_embedding
    )

    retrieved_docs = []

    for doc in results["documents"][0]:

        retrieved_docs.append({
            "text": doc,
            "company": "Placement Dataset",
            "section": "general"
        })

    fallback = fallback_response(
        retrieved_docs
    )

    if fallback:

        return {
            "answer": fallback,
            "sources": []
        }

    answer = generate_grounded_response(
        query,
        retrieved_docs
    )

    sources = extract_sources(
        retrieved_docs
    )

    return {
        "answer": answer,
        "sources": sources
    }