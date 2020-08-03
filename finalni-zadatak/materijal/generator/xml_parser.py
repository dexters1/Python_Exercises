import os.path
from lxml import etree
from lxml import objectify
import pickle

BLK_MAP = { "trapezoid": "izlaz", "rectangle": "obrada", "trapezoid2": "ulaz" }

def find_all_targets(node_name):
    L = []
    for edge in link_elements:
        source_node = edge.get("source")
        if source_node == node_name:
            L.append(edge.get("target"))
    return L
    
def find_all_sources(node_name):
    L = []
    for edge in link_elements:
        target_node = edge.get("target")
        if target_node == node_name:
            L.append(edge.get("source"))
    return L

#Opening and parsing xml file
file = open(os.path.dirname(os.path.realpath(__file__)) + '\..\sacasa.graphml','rb')
graph_root = objectify.parse(file)


#Finding useful elements inside the graph
link_elements = graph_root.findall("//{*}edge", )
bl_type_el = graph_root.findall(".//{*}Shape")
bl_name = graph_root.findall(".//{*}NodeLabel")
node_list = graph_root.findall(".//{*}node")
fn_type_el = graph_root.findall('.//{*}data[@key="d5"]')

print(etree.tostring(link_elements[0], pretty_print=True))
print(len(link_elements))

#appending useful information from elements inside the graph onto lists
block_type_list = []
for bl in bl_type_el:
    block_type_list.append(bl.get("type"))

bl_name_list = []
for bl in bl_name:
    bl_name_list.append(bl.text)

fn_list = []
for fn in fn_type_el:
    fn_list.append(fn)

#Going through all nodes of a graph and appending useful information onto the final list
elem = []
iterator = 0
for i in range(0, len(block_type_list)):
    L = []
    #append node name
    name = 'n' + str(i)
    L.append(name)
    
    #append block_type
    L.append(bl_name_list[i])
    
    #append function_type
    if "key=\"d5\"" in etree.tostring(node_list[i], pretty_print=True):
        if fn_type_el[iterator] == "":
            L.append("undefined_function")
            iterator = iterator + 1
        else:
            L.append(fn_type_el[iterator].text)
            iterator = iterator + 1
    else:
        L.append("undefined_function")
        
    L.append(BLK_MAP[block_type_list[i]])
    
    #append sources
    sources = find_all_sources(name)
    L.append(sources)
    #append targets
    targets = find_all_targets(name)
    L.append(targets)
    
    elem.append(L)
    
with open('xml_parsed.txt', 'w') as f:
    for item in elem:
        print >> f, item

with open('xml_pickle', 'wb') as f:
    pickle.dump(elem, f)

file.close()