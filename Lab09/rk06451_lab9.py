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

def listofNodes(graph):
    nodes = []
    for i in graph:
        nodes.append(i)
    return nodes
def listofEdges(graph):
    edges = []
    for i in graph:
        for j in range(len(graph[i])):
            temp = []
            temp.append(i)
            for k in range(len(graph[i][j])):
                temp.append(graph[i][j][k])
            temp2 = ((temp[1]),(temp[0]) ,(temp[2]))
            temp2 = tuple(temp2)
            if temp2 not in edges:
                temp = tuple(temp)
                edges.append(temp)
    return edges
def printIn_OutDegree(graph):
    string = ""

    for i in graph:
        indegre = 0
        out_degree = len(graph[i])
        for j in graph:
            for k in range(len(graph[j])):
                if graph[j][k][0] == i :
                    indegre += 1

        string += ((str(i) +' => In-Degree:'+ str(indegre)+","+ " Out-Degree "+ str(out_degree)) +'\n')
    return string
def printDegree(graph):
    string = ""
    for i in graph:
        degree = len(graph[i])
        string += (str(i) + ' => ' + str(degree) + '\n')
    return string

def getNeighbour(graph,node):
    neighbours = []
    for i in range (len(graph[node])):
        neighbours.append(graph[node][i][0])
    return neighbours
def getOutNeighbour(graph,node):
    neighbours = []
    for i in range(len(graph[node])):
        neighbours.append(graph[node][i][0])
    print(neighbours)
def getNeareseNeighbour(graph,node):
    lowest_dist = graph[node][0]
    for i in range(len(graph[node])):
        if graph[node][i][1] < lowest_dist[1]:
            lowest_dist = graph[node][i]
    return lowest_dist[0]
def getInNeighbour(graph,node):
    lst = []
    for i in graph:
        for j in range(len(graph[i])):
            if graph[i][j][0] == node:
                lst.append(i)
    print(lst)

def isNeighbour(graph,node1,node2):
    temp = 0
    for i in range(len(graph[node1])):
        if node2 == graph[node1][i][0]:
            temp += 1
    if temp > 0 :
        print(True)
    else:
        print(False)
def removeNode(graph, node):
    del graph[node]
    for i in graph:
        j = 0
        while j != len(graph[i]):
            if graph[i][j][0] == node :
                del graph[i][j]

            else:
                j += 1
    return graph
def removeNodes(graph,node):
    for i in range(len(node)):
        del graph[node[i]]
    for i in graph:
        j = 0
        while j != len(graph[i]):
            for k in range (len(node)):
                if j > len(graph[i])-1:
                    break
                if graph[i][j][0] == node[k]:
                    del graph[i][j]
                else:
                    j += 1
    return graph

def displayGraph(graph):
    print('G = {')
    for i in graph :
        print(f'{i} : {graph[i]},')
    print('}')

def display_adj_matrix(graph):
    adj_matrix = [[0 for i in range (len(graph))] for j in range (len(graph))]
    row = 0
    for i in graph:
        for j in range (len(graph[i])):
            column = helper_function_of_adj_matrix(graph,graph[i][j][0])
            adj_matrix[row][column] = 1
        row+=1

    for i in range(len(adj_matrix)):
        for j in range(len(adj_matrix)):
            print(adj_matrix[i][j],end = " ")
        print()
def helper_function_of_adj_matrix(graph,point):
    temp = 0
    for i in graph :
        if i == point:
            return temp
        temp += 1


nodes = ['BOS', 'ORD', 'JFK', 'DFW', 'MIA', 'SFO', 'LAX']
edges = [('BOS', 'JFK', 1) , ('BOS', 'MIA', 1), ('BOS', 'SFO', 1), ('JFK', 'BOS', 1),
('JFK', 'SFO', 1), ('JFK', 'MIA', 1), ('JFK', 'DFW', 1), ('ORD', 'MIA', 1),
('ORD', 'DFW', 1), ('MIA', 'DFW', 1), ('MIA', 'LAX', 1), ('DFW', 'ORD', 1),
('DFW', 'SFO', 1), ('DFW', 'LAX', 1), ('SFO', 'LAX', 1), ('LAX', 'ORD', 1)]
G = {}
print(addNodes(G,nodes))
print(addEdgs(G,edges,True))
print(listofNodes(G))
print(listofEdges(G))
print(printIn_OutDegree(G))
getInNeighbour(G, 'BOS')
getOutNeighbour(G, 'BOS')
isNeighbour(G, 'MIA', 'DFW')
isNeighbour(G, 'DFW', 'MIA')
