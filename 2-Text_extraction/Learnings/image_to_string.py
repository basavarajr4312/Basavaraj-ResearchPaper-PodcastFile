from PIL import Image
import pytesseract
import json

# img = Image.open("doc1_images/page_1.png")

# str = pytesseract.image_to_string(img)
# print(str)

results = {}
for i in range(1,3):
    img = Image.open(f"doc1_images/page_{i}.png")
    content = pytesseract.image_to_string(img)
    results[f"page_{i}_content"] = content
    print(f"Page {i} processing done...\n")

# formated_json = json.dumps(results)

with open("data.json",'w') as f:
    json.dump(results,f)