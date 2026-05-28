from src.chunking.semantic_chunker import create_chunks, attach_metadata


sample_text = """
Amazon offers 28.6 LPA package.
Google offers 42.0 LPA package.
Microsoft focuses on OS and DBMS.
"""


chunks = create_chunks(sample_text)

metadata_chunks = attach_metadata(
    chunks,
    company="Amazon",
    section="eligibility"
)

print(metadata_chunks)