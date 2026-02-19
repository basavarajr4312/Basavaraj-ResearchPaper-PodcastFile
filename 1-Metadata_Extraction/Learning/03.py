import fitz  # PyMuPDF

doc = fitz.open("doc.pdf")
meta = doc.metadata

print(doc.pages)

for key, value in meta.items():
    print(f"{key}: {value}")

doc.close()
