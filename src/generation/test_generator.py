from src.generation.generator import (
    generate_grounded_response
)


query = "What is Amazon package?"


retrieved_chunks = [

    {
        "text": "Amazon offers 28.6 LPA package"
    },

    {
        "text": "Amazon allows 1 backlog"
    }
]


response = generate_grounded_response(
    query,
    retrieved_chunks
)

print(response)
