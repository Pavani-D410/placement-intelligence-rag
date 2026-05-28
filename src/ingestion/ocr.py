import easyocr
import numpy as np

from pdf2image import convert_from_path


reader = easyocr.Reader(["en"])


def extract_text_from_images(pdf_path):

    images = convert_from_path(
    pdf_path,
    first_page=1,
    last_page=3)

    extracted_text = ""

    for image in images:

        image_np = np.array(image)

        results = reader.readtext(image_np)

        for result in results:

            extracted_text += result[1] + "\n"

    return extracted_text