from src.ingestion.ocr import (
    extract_text_from_images
)


pdf_path = (
    "data/raw/"
    "Placement_RAG_Dataset_Enhanced.pdf"
)


ocr_text = extract_text_from_images(
    pdf_path
)


with open(
    "cache/ocr_text.txt",
    "w",
    encoding="utf-8"
) as file:

    file.write(ocr_text)


print("OCR preprocessing completed.")