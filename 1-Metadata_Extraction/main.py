import pikepdf
import json

pdf_path = "doc.pdf"
result = {}
with pikepdf.open(pdf_path) as pdf:
    
    # standard metadata
    meta = pdf.docinfo
    for item in meta:
        result[str(item)] = str(meta[item])

with open("data.json",'w') as f:
    json.dump(result, f, )