from pdf2image import convert_from_path
import os

file_name = input("Enter PDF name from the parent directory of this project : ")

pdf_path = f"{file_name}.pdf"
output_folder_path = f"{file_name}_images"

os.makedirs(output_folder_path, exist_ok=True)

images = convert_from_path(pdf_path, dpi=300)

for i, image in enumerate(images):
    out_path = os.path.join(output_folder_path, f"page_{i+1}.png")
    image.save(out_path, 'PNG')