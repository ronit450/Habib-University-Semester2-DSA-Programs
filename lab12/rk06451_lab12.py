def push(lst, item):
    lst.append(item)
def pop(lst):
    if is_empty(lst) == False:
        return lst.pop()
    else:
        return False
def is_empty(lst):
    if len(lst) == 0:
        return True
    else:
        return False

# Copying Helper Functions from Lab 9
def addNodes(graph, nodes):
    key = []
    for i in nodes :
        graph[i] = list(key)
    return graph

def addEdgs(graph, edges, directed = False):
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

def Dijkstras(graph, starting_node):
    visited_node = []
# creating a list whose 1st index will be the visiting_node
# second index will be a distance
# third will be a parent node
    false_value = 0
    distance = 0
    dictionary_lst = {}
    for i in graph:
        dictionary_lst[i] = [False, 1000000, ""]
    visited_node.append(starting_node)
    last_node = starting_node
    dictionary_lst[starting_node][1] = 0
    temp_dst = []
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
            distance += dictionary_lst[last_node][1]
            if distance < dictionary_lst[i][1]:
                dictionary_lst[i][1] = distance
                dictionary_lst[i][2] = last_node
        last_node = get_the_smallest_distance_among_nodes(dictionary_lst)
        visited_node.append(last_node)
        false_value += 1
    return dictionary_lst
def getShortesetPath(graph,starting_node,ending_node):
    dictionary_lst = Dijkstras(graph,starting_node)
    print(dictionary_lst)
    path = []
    path.append(ending_node)
    last_node = ending_node
    while last_node!= starting_node:
        last_node = dictionary_lst[last_node][2]
        path.append(last_node)
    print(path)
    distance_for_journey = dictionary_lst[path[0]][1]
    print(distance_for_journey)
    path = (path[::-1])
    print(path)
    output_path = []
    for i in range(len(path)-1):
        temp = (path[i],path[i+1])
        output_path.append(temp)
    return output_path
def dfs_traversal(graph,starting_node):
    visited_nodes = []
    stack = []
    push(stack,starting_node)
    while is_empty(stack) == False:
        poped_element = pop(stack)
        lst_of_nodes = retrieving_edges(graph,poped_element)
        lst_of_nodes = sorted(lst_of_nodes)
        if poped_element not in visited_nodes:
            visited_nodes.append(poped_element)
        for i in lst_of_nodes:
            if i not in visited_nodes:
                push(stack,i)
    return visited_nodes
def exercise1():
    graph = {}
    nodes = ['A','B','C','D','E','F','G']
    addNodes(graph,nodes)
    edges = [
        ('A','B',5), ('A','E',6),('A','D',3),
        ('B','A',5), ('B','C',6),
        ('C', 'B', 6), ('C', 'D', 10), ('C', 'G', 2),
        ('D', 'C', 10), ('D', 'F', 8), ('D', 'A', 3),
        ('E', 'A', 6), ('E', 'F', 9),
        ('F', 'E', 9), ('F', 'D', 8), ('F', 'G', 10),
        ('G', 'F', 10), ('G', 'C', 2),
    ]
    addEdgs(graph,edges)
    print(getShortesetPath(graph,'A','G'))

def exercise1b():
    import csv
    lst = []
    graph = {}
    with open('connections.csv') as csv_file:
        file = csv.reader(csv_file)
        for i in file:
           lst.append(i)
    nodes = lst[0][1:]
    addNodes(graph,nodes)
    temp = 0
    edges = []
    for i in graph:
        temp += 1
        for j in range(1,len(lst[temp])):
            if int(lst[temp][j]) > 0 :
                temp2 = (i, nodes[j-1], int(lst[temp][j]))
                edges.append(temp2)
    addEdgs(graph,edges)
    print(getShortesetPath(graph,'Islamabad','Kaghan'))

def exercise2():
    graph = {}
    nodes = ['A','B','C','D','E','F','G']
    addNodes(graph,nodes)
    edges = [
        ('A','B',7), ('A','E',6),('A','D',2),
        ('B','A',7), ('B','C',3),
        ('C', 'B', 3), ('C', 'D', 2), ('C', 'G', 2),
        ('D', 'C', 2), ('D', 'F', 8), ('D', 'A', 2),
        ('E', 'A', 6), ('E', 'F', 9),
        ('F', 'E', 9), ('F', 'D', 8), ('F', 'G', 4),
        ('G', 'F', 4), ('G', 'C', 2),
    ]
    addEdgs(graph,edges)
    print(getShortesetPath(graph,'A','F'))

exercise1()



