import pickle
import os.path

def sort():
    with open(os.path.dirname(os.path.abspath(__file__)) + '\\xml_pickle', 'rb') as f:
        graph_info = pickle.load(f)

    #Set of all nodes with no incoming edge
    S = []
    #Empty list that will contain the sorted elements
    L = []

    #Append a node without an incoming edge to list S
    for node in graph_info:
        if not node[4]:
            S.append(node)

    #Find number of regular nodes in graph ( The ones not added by user )
    regular_node_num = -1
    for node in graph_info:
        if node[0][0] == 'n':
            regular_node_num = regular_node_num + 1
     
    #Sort nodes by execution order
    while len(S) > 0:
        temp = S[0]
        L.append(S.pop(0))
        for node in temp[5]:
            if "user_defined" in node:
                user_num = int(node[12:])
                S.append(graph_info[regular_node_num+user_num])
            else:
                S.append(graph_info[int(node[1:])])
        
    with open(os.path.dirname(os.path.abspath(__file__)) +'\\xml_pickle_sorted', 'wb') as f:
        pickle.dump(L, f)
