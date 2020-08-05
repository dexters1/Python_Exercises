import os.path
from lxml import etree
from lxml import objectify
import pickle

BLK_MAP = { "trapezoid": "izlaz", "rectangle": "obrada", "trapezoid2": "ulaz" }

#xml_user_defined moze samo da izmedju vec dve postojece veze stavi user_defined block
#Ova funkcija te postojece veze menja tako da prolaze kroz user_defined block
def edge_user_fix(link_elements):
    edge_id_target = []
    edge_id_source = []
    for edge in link_elements:
        if "user_defined" in edge.get("source"):
            edge_id_target.append(edge.get("target"))
        if "user_defined" in edge.get("target"):
            edge_id_source.append(edge.get("source"))
    for i in range(0, len(edge_id_source)):
        for edge in link_elements:
            if edge.get("source") == edge_id_source[i] and edge.get("target") == edge_id_target[i]:
                link_elements.remove(edge)
        
#Prolazi kroz sve ivice grafa i apenduje u listu sve ulazne ivice
def find_all_targets(node_name, link_elements):
    L = []
    for edge in link_elements:
        source_node = edge.get("source")
        if source_node == node_name:
            L.append(edge.get("target"))
    return L

#Prolazi kroz sve ivice grafa i apenduje u listu sve izlazne ivice    
def find_all_sources(node_name, link_elements):
    L = []
    for edge in link_elements:
        target_node = edge.get("target")
        if target_node == node_name:
            L.append(edge.get("source"))
    return L


def parse_xml(file_name):
    #Opening and parsing xml file
    file = open(os.path.dirname(os.path.abspath(__file__)) + '\..\..\\' + file_name, 'rb')
    graph_root = objectify.parse(file)

    #Adding UserDefined block 
    with open(os.path.dirname(os.path.abspath(__file__)) + "\\xml_user_defined.xml", "rb") as f:
        item_string = f.read()
        item = graph_root.find(".//{*}graph")
        item.append(etree.fromstring(item_string))
      
    user_defined = graph_root.find(".//{*}user_defined")


    #Finding useful elements inside the graph
    link_elements = graph_root.findall("//{*}edge", )

    #Modifies xml to accomodate new user_defined block
    edge_user_fix(link_elements) 

    #Finding useful elements inside the graph
    bl_type_el = graph_root.findall(".//{*}Shape")
    bl_name = graph_root.findall(".//{*}NodeLabel")
    node_list = graph_root.findall(".//{*}node")
    fn_type_el = graph_root.findall('.//{*}data[@key="d5"]')

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
    user_defined_iterator = 1
    for i in range(0, len(block_type_list)):
        L = []
        #append node name
        if "user_defined" in node_list[i].get("id"):
            name = 'user_defined' + str(user_defined_iterator)
            user_defined_iterator = user_defined_iterator + 1
            L.append(name)
        else:
            name = 'n' + str(i)
            L.append(name)
        
        #append block_type
        bl_name_list[i] = bl_name_list[i].replace(" ","_")
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
        
        #append block type according to BLK_MAP
        L.append(BLK_MAP[block_type_list[i]])
        
        #append sources
        sources = find_all_sources(name, link_elements)
        L.append(sources)
        #append targets
        targets = find_all_targets(name, link_elements)
        L.append(targets)
        
        elem.append(L)
        

    #Writes useful extracted information to a txt file    
    with open(os.path.dirname(os.path.abspath(__file__)) +'\\xml_parsed.txt', 'w') as f:
        for item in elem:
            print >> f, item
    #Writes the elem list with the extracted information to a file
    with open(os.path.dirname(os.path.abspath(__file__)) +'\\xml_pickle', 'wb') as f:
        pickle.dump(elem, f)

    file.close()
    
    return elem
    
