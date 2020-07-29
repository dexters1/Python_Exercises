import json

print("\nLoaded json object: \n")
with open('json_file.json', 'r') as f:
    json_obj = json.load(f)
    print json_obj
    
print("\nModified json object: \n")
json_obj["glossary"]["title"] = "Igor"
json_obj["glossary"]["GlossDiv"]["title"] = "Ilic"
print json_obj

with open('json_new_file.json', 'w') as f:
    json.dump(json_obj, f)