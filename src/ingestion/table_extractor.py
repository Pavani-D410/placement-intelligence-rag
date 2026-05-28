import pdfplumber


def extract_tables(pdf_path):

    extracted_tables = []

    with pdfplumber.open(pdf_path) as pdf:

        for page_number, page in enumerate(pdf.pages):

            tables = page.extract_tables()

            for table in tables:

                extracted_tables.append({
                    "page": page_number + 1,
                    "table": table
                })

    return extracted_tables