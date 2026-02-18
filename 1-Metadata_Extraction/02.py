import pikepdf
import json

pdf_path = "doc3.pdf"
result = {}
with pikepdf.open(pdf_path) as pdf:
    
    # standard metadata
    meta = pdf.docinfo
    for item in meta:
        result[str(item)] = str(meta[item])
        # print(f"{item} : {meta[item]}")
    
    
    # XML data
    # xml_meta = pdf.open_metadata()
    # for i, item in enumerate(xml_meta):
    #     readable = re.sub(r"\{.*?\}", "", item)
    #     result[readable] = xml_meta[item]
        
# for item in result:
#     print(f"{item} : {result[item]}")

with open("data.json",'w') as f:
    json.dump(result, f, )