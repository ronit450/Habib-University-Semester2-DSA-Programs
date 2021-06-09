# G is the graph that uses dictionary as a data structure
# nodes is the list that contains the keys of dictionary

def addNodes(G, nodes):
    for i in nodes:
        G[i] = []
    return G


# Edges contains a list of tuples that represents a connection between nodes
# default parameter, directed, tells whether or not the graph is a directed graph

def addEdges(G, edges, directed=False):
    if directed:
        for i in range(len(edges)):
            G[edges[i][0]].append((edges[i][1], edges[i][2]))
    else:
        for i in range(len(edges)):
            G[edges[i][0]].append((edges[i][1], edges[i][2]))
            G[edges[i][1]].append((edges[i][0], edges[i][2]))
    return G


# returns the area graph that connects the areas of Karachi together

def getAreaGraph():
    G = {}
    Nodes = [
        'Saddar', 'Defence(Ph1,Ph2)', 'Defence(Ph4,Ph5,Gizri)', 'North Nazimabad', 'Gulshan e Iqbal',
        'Garden', 'Habib University', 'Malir Cantt', 'Defence(Ph6,Ph7,Ph8)', 'Clifton Block (1,2,3)',
        'Bahadurabad', 'PECHS', 'Shaheed e Millat', 'Federal B Area', 'Shahrah e Faisal', 'Gulistan e Johar',
        'Clifton Block (7,8,9)', 'Clifton Cantt'
    ]
    Edges = [
        ('Saddar', 'Shahrah e Faisal', 16),
        ('Saddar', 'PECHS', 5),
        ('Saddar', 'Shaheed e Millat', 6),
        ('Saddar', 'Gulistan e Johar', 14),
        ('Saddar', 'Bahadurabad', 7),
        ('Saddar', 'North Nazimabad', 10),
        ('Saddar', 'Federal B Area', 9),
        ('Saddar', 'Gulshan e Iqbal', 11),
        ('Defence(Ph1,Ph2)', 'Shaheed e Millat', 7),
        ('Defence(Ph1,Ph2)', 'Shahrah e Faisal', 11.5),
        ('Defence(Ph1,Ph2)', 'Clifton Block (1,2,3)', 8),
        ('Defence(Ph1,Ph2)', 'Clifton Block (7,8,9)', 5),
        ('Defence(Ph1,Ph2)', 'Clifton Cantt', 6),
        ('Defence(Ph1,Ph2)', 'PECHS', 6),
        ('Defence(Ph1,Ph2)', 'Saddar', 6),
        ('Defence(Ph4,Ph5,Gizri)', 'Shaheed e Millat', 10),
        ('Defence(Ph4,Ph5,Gizri)', 'Shahrah e Faisal', 15),
        ('Defence(Ph4,Ph5,Gizri)', 'Saddar', 8),
        ('Defence(Ph4,Ph5,Gizri)', 'PECHS', 8),
        ('Defence(Ph4,Ph5,Gizri)', 'Clifton Block (1,2,3)', 7),
        ('Defence(Ph4,Ph5,Gizri)', 'Clifton Block (7,8,9)', 3),
        ('Defence(Ph4,Ph5,Gizri)', 'Clifton Cantt', 3),
        ('Defence(Ph6,Ph7,Ph8)', 'Shaheed e Millat', 9),
        ('Defence(Ph6,Ph7,Ph8)', 'Shahrah e Faisal', 15.5),
        ('Defence(Ph6,Ph7,Ph8)', 'Saddar', 8),
        ('Defence(Ph6,Ph7,Ph8)', 'Clifton Block (1,2,3)', 10),
        ('Defence(Ph6,Ph7,Ph8)', 'Clifton Block (7,8,9)', 9),
        ('Defence(Ph6,Ph7,Ph8)', 'Clifton Cantt', 5),
        ('Defence(Ph6,Ph7,Ph8)', 'PECHS', 16),
        ('Clifton Block (1,2,3)', 'Saddar', 8),
        ('Clifton Block (1,2,3)', 'Shaheed e Millat', 13),
        ('Clifton Block (1,2,3)', 'Shahrah e Faisal', 15.5),
        ('Clifton Block (1,2,3)', 'PECHS', 10),
        ('Clifton Block (7,8,9)', 'Shaheed e Millat', 9),
        ('Clifton Block (7,8,9)', 'Shahrah e Faisal', 13),
        ('Clifton Block (7,8,9)', 'Saddar', 5),
        ('Clifton Block (7,8,9)', 'PECHS', 7),
        ('Clifton Cantt', 'Saddar', 9),
        ('Clifton Cantt', 'Shaheed e Millat', 13),
        ('Clifton Cantt', 'Shahrah e Faisal', 14.5),
        ('North Nazimabad', 'Gulshan e Iqbal', 10),
        ('North Nazimabad', 'Defence(Ph1,Ph2)', 16),
        ('North Nazimabad', 'Defence(Ph4,Ph5,Gizri)', 17),
        ('North Nazimabad', 'Defence(Ph6,Ph7,Ph8)', 25),
        ('North Nazimabad', 'Clifton Block (1,2,3)', 18),
        ('North Nazimabad', 'Clifton Block (7,8,9)', 15),
        ('North Nazimabad', 'Clifton Cantt', 18),
        ('Malir Cantt', 'North Nazimabad', 25),
        ('Malir Cantt', 'Gulshan e Iqbal', 18),
        ('Malir Cantt', 'Bahadurabad', 21),
        ('Malir Cantt', 'Gulistan e Johar', 12),
        ('Federal B Area', 'Gulshan e Iqbal', 6),
        ('Federal B Area', 'Bahadurabad', 12),
        ('Federal B Area', 'North Nazimabad', 5),
        ('Federal B Area', 'Defence(Ph1,Ph2)', 17),
        ('Federal B Area', 'Defence(Ph4,Ph5,Gizri)', 19),
        ('Federal B Area', 'Defence(Ph6,Ph7,Ph8)', 27),
        ('Federal B Area', 'Clifton Block (1,2,3)', 22),
        ('Federal B Area', 'Clifton Block (7,8,9)', 17),
        ('Federal B Area', 'Clifton Cantt', 22),
        ('PECHS', 'Bahadurabad', 2),
        ('PECHS', 'Shahrah e Faisal', 10),
        ('PECHS', 'Shaheed e Millat', 2),
        ('Garden', 'Saddar', 3),
        ('Garden', 'Shahrah e Faisal', 14),
        ('Garden', 'Shaheed e Millat', 6),
        ('Garden', 'North Nazimabad', 7),
        ('Garden', 'Defence(Ph1,Ph2)', 9),
        ('Garden', 'Defence(Ph4,Ph5,Gizri)', 9),
        ('Garden', 'Defence(Ph6,Ph7,Ph8)', 16),
        ('Garden', 'Clifton Block (1,2,3)', 10),
        ('Garden', 'Clifton Block (7,8,9)', 7),
        ('Garden', 'Clifton Cantt', 6),
        ('Bahadurabad', 'Shaheed e Millat', 2),
        ('Bahadurabad', 'North Nazimabad', 10),
        ('Bahadurabad', 'Defence(Ph1,Ph2)', 8),
        ('Bahadurabad', 'Defence(Ph4,Ph5,Gizri)', 12),
        ('Bahadurabad', 'Defence(Ph6,Ph7,Ph8)', 16),
        ('Bahadurabad', 'Clifton Block (1,2,3)', 15),
        ('Bahadurabad', 'Clifton Block (7,8,9)', 11),
        ('Bahadurabad', 'Clifton Cantt', 7),
        ('Gulshan e Iqbal', 'Defence(Ph1,Ph2)', 18.5),
        ('Gulshan e Iqbal', 'Defence(Ph4,Ph5,Gizri)', 19),
        ('Gulshan e Iqbal', 'Defence(Ph6,Ph7,Ph8)', 19),
        ('Gulshan e Iqbal', 'Clifton Block (1,2,3)', 18),
        ('Gulshan e Iqbal', 'Clifton Block (7,8,9)', 15),
        ('Gulshan e Iqbal', 'Clifton Cantt', 14),
        ('Shahrah e Faisal', 'Gulshan e Iqbal', 8),
        ('Shahrah e Faisal', 'Gulistan e Johar', 11),
        ('Shaheed e Millat', 'Bahadurabad', 4),
        ('Shaheed e Millat', 'Gulistan e Johar', 12),
        ('Shahrah e Faisal', 'Habib University', 6),
        ('Gulshan e Iqbal', 'Gulistan e Johar', 5),
        ('Gulistan e Johar', 'Habib University', 0.5)
    ]
    G = addNodes(G, Nodes)
    G = addEdges(G, Edges)
    return G


# It will give all the edges connected to a particular node.

def retrieving_edges(graph, node):
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


# Dijksta algorithm will run over the graph. It will give the shortest path to each area.

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
            count += 1
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

# returns the shortest path from starting node till ending node in the graph we get by calling the function
# getAreaGraph()


def getShortesetPath(starting_node, ending_node, graph=getAreaGraph()):
    dictionary_lst = Dijkstras(graph, starting_node)
    path = []
    path.append(ending_node)
    last_node = ending_node
    while last_node != starting_node:
        last_node = dictionary_lst[last_node][2]
        path.append(last_node)
    distance_for_journey = dictionary_lst[path[0]][1]
    output_path = path[::-1]
    return output_path, distance_for_journey

# def temp_main(starting_area):
    # return getShortesetPath(Areas, starting_area, 'Habib University')


#Areas = getAreaGraph()
# print(getShortesetPath(Areas, 'Saddar', 'Habib University')) #Test Case
