from table_extractor import extract_tables


pdf_path = "data/raw/Placement_RAG_Dataset_Enhanced.pdf"

tables = extract_tables(pdf_path)

print(tables[:2])