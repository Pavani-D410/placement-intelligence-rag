from src.reasoning.conflict_detector import (
    detect_conflicts
)


chunks = [

    {
        "company": "Amazon",
        "text": "Amazon minimum CGPA is 6.4"
    },

    {
        "company": "Amazon",
        "text": "Amazon minimum CGPA is 7.0"
    }
]


results = detect_conflicts(chunks)

print(results)