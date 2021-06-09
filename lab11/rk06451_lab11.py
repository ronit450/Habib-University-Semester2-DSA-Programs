# Copying Helper Functions frrom Lab 9
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

# Copying Stack_methods/Functions
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

# Copying Queue Functions
def enQueue(lst, data):
    lst.append(data)


def deQueue(lst):
    if is_empty(lst) == False:
        return lst.pop(0)
    else:
        return False
def retrieving_edges(graph,node):
    lst_of_nodes = []
    for i in range(len(graph[node])):
        lst_of_nodes.append(graph[node][i][0])
    return lst_of_nodes

def bfs_traversal(graph,starting_node):
    visited_nodes = []
    queue = []
    enQueue(queue,starting_node)
    while is_empty(queue) == False:
        dequeued_element = deQueue(queue)
        lst_of_nodes = retrieving_edges(graph, dequeued_element)
        if dequeued_element not in visited_nodes:
            visited_nodes.append(dequeued_element)
        for i in lst_of_nodes:
            if i not in visited_nodes:
                enQueue(queue, i)
    return visited_nodes

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
def bfs_levels(graph):
    levels= {}
    for i in graph:
        temp_level = 0
        for j in graph:
            if j != i :
                for k in range(len(graph[j])):
                    if graph[j][k][0] == i :
                        if j in levels :
                            temp_level += levels[j] +1
        levels[i] = temp_level
    return levels
def finding_bfs_levels(graph,level_number):
    levels = bfs_levels(graph)
    lst_with_level = []
    for i in levels:
        if levels[i] == level_number:
            lst_with_level.append(i)
    return lst_with_level
def finding_bfs_levels_with_node(graph,node):
    levels = bfs_levels(graph)
    return levels[node]
def finding_cycle(graph,lst_of_cycle):
    first_node = lst_of_cycle[0]
    last_node = lst_of_cycle[len(lst_of_cycle)-1]
    for i in range (len(graph[first_node])):
        if graph[first_node][i][0] == last_node:
            return 'Yes'

    return 'No'
def exercise1():
    graph = {}
    nodes = [0,1,2,3,4,5]
    addNodes(graph,nodes)
    edges = [(0,1),(0,2),(1,2),(1,3),(2,4),(3,4),(3,5),(4,5)]
    addEdgs(graph,edges)
    print(dfs_traversal(graph,0))
def exercise2():
    graph = {}
    nodes = ['Austin', 'Atlanta', 'Chicago', 'Dallas', 'Denver', 'Houston', 'Washington']
    addNodes(graph, nodes)
    edges = [('Austin', 'Dallas', 200), ('Austin', 'Houston', 160), ('Atlanta', 'Washington', 600),
             ('Atlanta', 'Houston', 800),
             ('Chicago', 'Denver', 1000), ('Dallas', 'Austin', 200), ('Dallas', 'Denver', 780),
             ('Dallas', 'Chicago', 900),
             ('Denver', 'Chicago', 1000), ('Denver', 'Atlanta', 1400),
             ('Houston', 'Atlanta', 800), ('Washington', 'Dallas', 1300), ('Washington', 'Atlanta', 600)]
    addEdgs(graph, edges)
    lst = ['Houston','Austin','Atlanta','Washington','Dallas']
    print(finding_cycle(graph,lst))
def exercise3():
    graph = {}
    nodes = ['S','1','2','3','4','5','6','7']
    addNodes(graph,nodes)
    edges = [
        ('S','1'),('S','2'),('1','3'),('1','4'),('1','5'),('2','6'),('6','7')
        ]
    addEdgs(graph,edges)
    print(graph)
    print(bfs_traversal(graph,'S'))

def exercise4():
    graph = {}
    nodes = ['S', '1', '2', '3', '4', '5', '6', '7']
    addNodes(graph, nodes)
    edges = [
        ('S', '1'), ('S', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '6'), ('6', '7')
    ]
    addEdgs(graph, edges)
    print(finding_bfs_levels(graph, 1))
def exercise4b():
    graph = {}
    nodes = ['S', '1', '2', '3', '4', '5', '6', '7']
    addNodes(graph, nodes)
    edges = [
        ('S', '1'), ('S', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '6'), ('6', '7')
    ]
    addEdgs(graph, edges)
    print(graph)
    print(finding_bfs_levels_with_node(graph,'6'))
exercise3()

