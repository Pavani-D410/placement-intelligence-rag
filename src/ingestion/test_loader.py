from pdf_loader import load_pdf


pdf_path = "data/raw/Placement_RAG_Dataset_Enhanced.pdf"

text = load_pdf(pdf_path)

print(text[:3000])