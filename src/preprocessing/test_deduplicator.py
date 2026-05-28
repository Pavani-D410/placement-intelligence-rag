from deduplicator import remove_duplicates


sample_chunks = [
    "Amazon interview experience",
    "Amazon interview experience",
    "Google interview process"
]

clean_chunks = remove_duplicates(sample_chunks)

print(clean_chunks)