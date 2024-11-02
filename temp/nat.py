import json


with open("nationalities.json", "r") as f:
    n = json.loads(f.read())

print("[")
for item in n:
    print('"' + item["name"]["common"] + '"' + ",")

print("]")
