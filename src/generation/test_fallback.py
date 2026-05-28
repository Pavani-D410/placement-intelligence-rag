from src.generation.fallback import (
    fallback_response
)


chunks = []


response = fallback_response(chunks)

print(response)