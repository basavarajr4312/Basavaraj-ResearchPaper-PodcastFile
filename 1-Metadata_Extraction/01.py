from pypdf import PdfReader

path = "doc3.pdf"

reader = PdfReader(path)

info = reader.metadata

num_pages = len(reader.pages)
print("Number of pages:", num_pages)

for key, value in info.items():
    print(f"{key}: {value}")


