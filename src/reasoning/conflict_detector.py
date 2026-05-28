def detect_conflicts(retrieved_chunks):

    conflicts = []

    seen = {}

    for chunk in retrieved_chunks:

        company = chunk["company"]

        text = chunk["text"]

        if company not in seen:

            seen[company] = text

        else:

            if seen[company] != text:

                conflicts.append({
                    "company": company,
                    "conflict": [
                        seen[company],
                        text
                    ]
                })

    return conflicts