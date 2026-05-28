from src.retrieval.metadata_filter import (
    filter_by_metadata
)


chunks = [
    {
        "text": "Amazon offers 28.6 LPA",
        "company": "Amazon",
        "section": "eligibility"
    },

    {
        "text": "Google offers 42.0 LPA",
        "company": "Google",
        "section": "eligibility"
    }
]


results = filter_by_metadata(
    chunks,
    company="Amazon"
)

print(results)