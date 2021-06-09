def addNodes(graph, nodes):
    key = []
    for i in nodes :
        graph[i] = list(key)
    return graph

def addEdgs(graph, edges):
    for i in range(len(edges)):
        if edges[i][0] in graph:
            temp = []
            if len(edges[i]) != 3 :
                edges[i] = list(edges[i])
                edges[i].append(1)
                edges[i] = tuple(edges[i])
            for j in range(1,len(edges[i])):
                temp.append(edges[i][j])
            temp = tuple(temp)
            graph[edges[i][0]].append(temp)
    return graph
def retrieving_edges(graph,node):
    lst_of_nodes = []
    for i in range(len(graph[node])):
        lst_of_nodes.append(graph[node][i][0])
    return lst_of_nodes
def get_the_smallest_distance_among_nodes(graph):
    smallest = 100000000000
    node = ""
    for i in graph:
        if graph[i][0] == False:
            if graph[i][1] < smallest:
                smallest = graph[i][1]
                node = i
    return node
def shortest_distance_for_kruskal(graph):
    smallest = 10000000
    for i in graph:
        for j in range(len(graph[i])):
            if graph[i][j][1] < smallest:
                smallest = graph[i][j][1]
                edge = (i,graph[i][j][0],graph[i][j][1])
    return edge
def get_the_largest_distance_among_nodes(graph):
    largest = 0
    node = ""
    for i in graph:
        if graph[i][0] == False:
            if graph[i][1] > largest:
                largest = graph[i][1]
                node = i
    return node
def Prims_algorithm(graph, starting_node,modified):
    visited_node = []
# creating a list whose 1st index will be the visiting_node
# second index will be a distance
# third will be a parent node
    false_value = 0
    distance = 0
    dictionary_lst = {}
    for i in graph:
        if modified == False:
            dictionary_lst[i] = [False, 1000000, ""]
        elif modified == True:
            dictionary_lst[i] = [False,0,""]
    visited_node.append(starting_node)
    last_node = starting_node
    dictionary_lst[starting_node][1] = 0
    while false_value != len(graph):
        dictionary_lst[last_node][0] = True
        retrieving_nodes = retrieving_edges(graph, last_node)
        count = 0
        for s in retrieving_nodes:
            if s in visited_node:
                retrieving_nodes.pop(count)
            count+=1

        for i in retrieving_nodes:
            for j in range(len(graph[last_node])):
                if graph[last_node][j][0] == i:
                    distance = graph[last_node][j][1]
                    break
            if modified == False:
                if distance < dictionary_lst[i][1]:
                    dictionary_lst[i][1] = distance
                    dictionary_lst[i][2] = last_node
            else:
                if distance > dictionary_lst[i][1]:
                    dictionary_lst[i][1] = distance
                    dictionary_lst[i][2] = last_node
        if modified == False:
            last_node = get_the_smallest_distance_among_nodes(dictionary_lst)
        else:
            last_node = get_the_largest_distance_among_nodes(dictionary_lst)
        visited_node.append(last_node)
        false_value += 1
    return dictionary_lst
def MSTPRIMS(graph,starting_node):
    dictonary_lst = Prims_algorithm(graph,starting_node,False)
    minimum_spaning_tree = []
    print(dictonary_lst)
    for i in dictonary_lst:
        for j in dictonary_lst:
            if j != i:
                if dictonary_lst[j][2] == i :
                    temp_tupple = (i,j, dictonary_lst[j][1])
                    minimum_spaning_tree.append(temp_tupple)
    return minimum_spaning_tree
def MSTPRIMMAX(graph,starting_node):
    dictionary_lst = Prims_algorithm(graph,starting_node,True)
    maximumm_spaning_tree = []
    for i in dictionary_lst:
        for j in dictionary_lst:
            if j != i:
                if dictionary_lst[j][2] == i:
                    temp_tupple = (i, j, dictionary_lst[j][1])
                    maximumm_spaning_tree.append(temp_tupple)
    return maximumm_spaning_tree
def remove_the_shortest_node(graph , node):
    temp = 1
    for i in node:
        for j in range(len(graph[i])):
            if graph[i][j][0] == node[temp]:
                del graph[i][j]
                temp -= 1
                break

    return graph
def checking_cycle(set_of_nodes,edge):
    index_add_to = 0
    index_from_to = 0
    for i in range(len(set_of_nodes)):
        if edge[0] in set_of_nodes[i] and edge[1] not in set_of_nodes[i]:
            index_add_to = i
        elif edge[0] in set_of_nodes[i] and edge[1] in set_of_nodes[i]:
            return set_of_nodes,False
        if edge[1] in set_of_nodes[i]:
            index_from_to = i
    for i in set_of_nodes[index_from_to]:
        set_of_nodes[index_add_to].append(i)
    del set_of_nodes[index_from_to]
    return set_of_nodes,True

def MSTKruskal(graph):
    minimum_spanning_tree = []
    nodes_of_graph = [[i] for i in graph]
    x = False
    while len(nodes_of_graph) != 1:
        while x == False:
            temp = shortest_distance_for_kruskal(graph)
            temp_edge = temp[0:2]
            result = checking_cycle(nodes_of_graph,temp)
            nodes_of_graph = result[0]
            if result[1] == True:
                minimum_spanning_tree.append(temp)
                remove_the_shortest_node(graph,temp_edge)
                break
            else:
                remove_the_shortest_node(graph,temp_edge)
    return minimum_spanning_tree
def convert_adjmatrix_to_adjlst(matrix):
    graph = {}
    temp_for_row = 1
    for i in range (len(matrix)):
        graph[temp_for_row] = []
        temp_for_column= 1
        for j in range(len(matrix)):
            if matrix[i][j]!= 0:
                edge = (temp_for_column,matrix[i][j])
                graph[temp_for_row].append(edge)
            temp_for_column+=1
        temp_for_row+=1
    return graph
def exercise1():
    graph = {}
    nodes = ['A','B','C','D','E','F','G']
    addNodes(graph, nodes)
    edges = [
        ('A','B',5), ('A','E',6), ('A','D',3),
        ('B', 'A',5),('B', 'C',6),
        ('C', 'B', 6), ('C', 'D', 10),('C', 'G', 2),
        ('D','A', 3), ('D', 'F', 8),('D','C', 10),
        ('E','A', 6), ('E', 'F', 9),
        ('F','E', 9), ('F', 'G', 10), ('F','D', 8),
        ('G','C', 2), ('G','F', 10),
        ]
    addEdgs(graph,edges)
    print(MSTPRIMS(graph,'A'))
def exercise1c():
    graph = {}
    nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    addNodes(graph, nodes)
    edges = [
        ('A', 'B', 5), ('A', 'E', 6), ('A', 'D', 3),
        ('B', 'A', 5), ('B', 'C', 6),
        ('C', 'B', 6), ('C', 'D', 10), ('C', 'G', 2),
        ('D', 'A', 3), ('D', 'F', 8), ('D', 'C', 10),
        ('E', 'A', 6), ('E', 'F', 9),
        ('F', 'E', 9), ('F', 'G', 10), ('F', 'D', 8),
        ('G', 'C', 2), ('G', 'F', 10),
    ]
    addEdgs(graph, edges)
    print(MSTPRIMMAX(graph, 'A'))
def exercise2():
    graph = {}
    nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    addNodes(graph, nodes)
    edges = [
        ('A', 'B', 5), ('A', 'E', 6), ('A', 'D', 3),
        ('B', 'A', 5), ('B', 'C', 6),
        ('C', 'B', 6), ('C', 'D', 10), ('C', 'G', 2),
        ('D', 'A', 3), ('D', 'F', 8), ('D', 'C', 10),
        ('E', 'A', 6), ('E', 'F', 9),
        ('F', 'E', 9), ('F', 'G', 10), ('F', 'D', 8),
        ('G', 'C', 2), ('G', 'F', 10),
    ]
    addEdgs(graph, edges)
    print(MSTKruskal(graph))
def exercise3():
    adj_matrix = [
        [0,240,210,340,280,200,345,120],
        [0,0,265,175,215,180,185,155],
        [0,0,0,260,115,350,435,195],
        [0,0,0,0,160,330,295,230],
        [0,0,0,0,0,360,400,170],
        [0,0,0,0,0,0,175,205],
        [0,0,0,0,0,0,0,305],
        [0,0,0,0,0,0,0,0]
    ]
    graph = convert_adjmatrix_to_adjlst(adj_matrix)
    print(graph)
    print(MSTKruskal(graph))
    # Minimum Spanning tree with prims algorithm
    print(MSTPRIMS(graph,1))
exercise3()