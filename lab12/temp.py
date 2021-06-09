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
    path = []
    path.append(ending_node)
    last_node = ending_node
    while last_node!= starting_node:
        last_node = dictionary_lst[last_node][2]
        path.append(last_node)
    distance_for_journey = dictionary_lst[path[0]][1]
    output_path = path[::-1]
    return output_path, distance_for_journey