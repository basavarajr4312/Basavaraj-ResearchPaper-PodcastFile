from pdf2image import convert_from_path
import pytesseract
import json
import fitz # for metadata

file_name = "doc1"

pdf_path = f"{file_name}.pdf"
output_folder_path = f"{file_name}_images"

images = convert_from_path(pdf_path, dpi=300)

result = {}



doc = fitz.open(f"{file_name}.pdf")
meta = doc.metadata

for key, value in meta.items():
    if value != "":
        result[key] = value

doc.close()

def pdf_to_image():
    pages_content = []
    for i, image in enumerate(images):

        print(f"\nPage {i+1} processing going on....")
        page_content = pytesseract.image_to_string(image)
        print(f"Page {i+1} processing done.")

        # result[f"page_{i+1}_content"] = page_content
        pages_content.append(page_content)
    return pages_content

pages_content = pdf_to_image()
result["pages_content"] = pages_content


with open("data.json",'w') as f:
    json.dump(result,f)