"""
Specification of functions we want to generate
""" 
import pickle
import os.path

functions = []
user_defined = []
all_functions = []

def function_spec():
    with open(os.path.dirname(os.path.abspath(__file__)) + '\..\\xml\\xml_pickle_sorted', 'rb') as f:
        graph_info = pickle.load(f)
    
    del functions[:]
    del user_defined[:]
    del all_functions[:]
    
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
            all_functions.append(dictionary)
        else:
            dictionary = {
                          "name": item[2],
                          "return_type": "float",
                          "include": "math.h",
                          "call_type": "float a",
                          }
            user_defined.append(dictionary)
            all_functions.append(dictionary)