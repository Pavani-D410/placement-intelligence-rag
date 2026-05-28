from src.ingestion.ocr import (
    extract_text_from_images
)


pdf_path = (
    "data/raw/"
    "Placement_RAG_Dataset_Enhanced.pdf"
)


text = extract_text_from_images(
    pdf_path
)


print("\n===== OCR OUTPUT =====\n")

print(text[:3000])