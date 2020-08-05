"""
Specification of functions we want to generate
""" 
import pickle
import os.path
with open(os.path.dirname(os.path.realpath(__file__)) + '\..\\xml_pickle', 'rb') as f:
    graph_info = pickle.load(f)
    
print(graph_info)

functions = []
user_defined = []

for item in graph_info:
    if not ("user_defined" in item[0]):
        if(item[2] == "undefined_function"):
            if item[3] == "ulaz":
                dictionary = {
                      "name": item[1],
                      "return_type": "float",
                      "include": "math.h",
                      }
            elif item[3] == "obrada":
                dictionary = {
                      "name": item[1],
                      "return_type": "float",
                      "include": "math.h",
                      "call_type": "float a",
                      }
            else:
                dictionary = {
                      "name": item[1],
                      "return_type": "void",
                      "include": "math.h",
                      "call_type": "float a",
                      }
        else:
            if item[3] == "ulaz":
                dictionary = {
                      "name": item[2],
                      "return_type": "float",
                      "include": "math.h",
                      }
            elif item[3] == "obrada":
                dictionary = {
                      "name": item[2],
                      "return_type": "float",
                      "include": "math.h",
                      "call_type": "float a",
                      }
            else:
                dictionary = {
                      "name": item[2],
                      "return_type": "void",
                      "include": "math.h",
                      "call_type": "float a",
                      }      
        functions.append(dictionary)
    else:
        dictionary = {
                      "name": item[2],
                      "return_type": "float",
                      "include": "math.h",
                      "call_type": "float a",
                      }
        user_defined.append(dictionary)