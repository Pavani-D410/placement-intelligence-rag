from src.generation.citations import (
    extract_sources
)


chunks = [

    {
        "company": "Amazon",
        "section": "eligibility"
    },

    {
        "company": "Google",
        "section": "interview"
    }
]


sources = extract_sources(chunks)

print(sources)