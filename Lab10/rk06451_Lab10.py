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
    sum_of_out_degree = 0
    sum_of_indegree = 0
    lst_of_indegree = {}
    lst_of_outdegree = {}
    for i in graph:
        indegre = 0
        out_degree = len(graph[i])
        lst_of_outdegree[i] = (out_degree)
        sum_of_out_degree += out_degree
        for j in graph:
            for k in range(len(graph[j])):
                if graph[j][k][0] == i :
                    indegre += 1
                    sum_of_indegree += 1
                lst_of_indegree[i] = indegre
        string += ((str(i) +' => In-Degree:'+ str(indegre)+","+ " Out-Degree "+ str(out_degree)) +'\n')
    return string, sum_of_out_degree, sum_of_indegree, lst_of_indegree , lst_of_outdegree
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
    return neighbours
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
    return lst

def isNeighbour(graph,node1,node2):
    temp = 0
    for i in range(len(graph[node1])):
        if node2 == graph[node1][i][0]:
            temp += 1
    if temp > 0 :
        return True
    else:
        return False
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

def maximum_inbound_and_outbound(lst_of_out_degree,lst_of_in_degree,node):
    maximum_out_bound = lst_of_out_degree[node]
    maximum_in_degree = lst_of_in_degree[node]
    lst_for_maximum_out_bound = []
    lst_for_maximum_in_bound = []
    for i in lst_of_out_degree:
        if maximum_out_bound < lst_of_out_degree[i]:
            maximum_out_bound = lst_of_out_degree[i]
            lst_for_maximum_out_bound = i
        elif maximum_out_bound == lst_of_out_degree[i]:
            lst_for_maximum_out_bound.append(i)
    for i in lst_of_in_degree:
        if maximum_in_degree < lst_of_out_degree[i]:
            maximum_in_degree = lst_of_in_degree[i]
            lst_for_maximum_in_bound = (i)
        elif maximum_in_degree == lst_of_in_degree[i]:
            lst_for_maximum_in_bound.append(i)
    return lst_for_maximum_out_bound , lst_for_maximum_in_bound


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
def one_way_airports(graph):
    pair = []
    for i in graph:
        for j in range(len(graph[i])):
            temp = 0
            checking_airpot = graph[i][j][0]
            for k in range (len(graph[checking_airpot])):
                if i != graph[checking_airpot][k][0]:
                    temp += 1
            if temp == len(graph[checking_airpot]):
                temp2 = (i,checking_airpot)
                pair.append(temp2)
    return pair
def connection_of_airpot(graph,node):
    final_lst = []
    neighbour  = getInNeighbour(graph,node)
    for i in neighbour:
        final_lst.append(i)
        temp = getInNeighbour(graph, i)
        for j in temp:
            if j != node:
                final_lst.append(j)
    return final_lst

def nearest_airpot(graph):
    for i in graph:
        print("The nearest neighbout from ", i, "Airpot is ", getNeareseNeighbour(graph, i))

def exercise1():
    graph = {}
    nodes = [1, 2, 3, 4, 5]
    edges = [(1, 2,1), (1, 5,1), (2, 1,1), (2, 3,1), (2, 4,1), (2, 5,1), (3, 2,1), (3, 4,1),
             (4, 2,1), (4, 3,1), (4, 5,1), (5, 1,1), (5, 2,1), (5, 4,1)]
    addNodes(graph, nodes)
    addEdgs(graph, edges)
    lst_of_nodes = listofNodes(graph)
    print(lst_of_nodes)
    print(listofEdges(graph))
    display_adj_matrix(graph)
    displayGraph(graph)
    indegree_lst = printIn_OutDegree(graph)[3]
    for i in lst_of_nodes:
        print(i, ": "+ " Neighbours => " + str(getOutNeighbour(graph, i))+ ',' + " Degree: " + str(indegree_lst[i]) )

def exercise2():
    graph = {}
    nodes = [1, 2, 3, 4]
    edges = [(1, 2,), (2, 4), (3, 1), (3, 2), (4, 3), (4, 4)]
    addNodes(graph,nodes)
    addEdgs(graph,edges)
    displayGraph(graph)
    print((printIn_OutDegree(graph))[0])
    for i in nodes:
        print(str(i) + ' : ' + str(getNeighbour(graph,i)) + ',')
    sum_of_out_degree = printIn_OutDegree(graph)[1]
    sum_of_in_degree = printIn_OutDegree(graph)[2]
    if sum_of_out_degree == len(edges) and sum_of_in_degree == len(edges):
        print(True)
    else:
        print(False)

def exercise3():
    graph = {}
    nodes = ['Austin', 'Atlanta', 'Chicago', 'Dallas', 'Denver', 'Houston', 'Washington']
    addNodes(graph, nodes)
    edges = [('Austin', 'Dallas', 200), ('Austin', 'Houston', 160), ('Atlanta', 'Washington', 600),
             ('Atlanta', 'Houston', 800),
             ('Chicago', 'Denver', 1000), ('Dallas', 'Austin', 200), ('Dallas', 'Denver', 780), ('Dallas' ,'Chicago',900),
             ('Denver', 'Chicago', 1000), ('Denver', 'Atlanta', 1400),
             ('Houston', 'Atlanta', 800), ('Washington', 'Dallas', 1300), ('Washington', 'Atlanta', 600)]
    addEdgs(graph, edges)
    lst_for_in_degree = printIn_OutDegree(graph)[3]
    lst_for_out_degree = printIn_OutDegree(graph)[4]
    displayGraph(graph)
    temp = maximum_inbound_and_outbound(lst_for_out_degree, lst_for_in_degree, nodes[0])
    print("The Airpot which has highest Outbound is ", temp[0])
    print("The Airpot which has highest Inbound is ", temp[1])
    print(one_way_airports(graph))
    nearest_airpot(graph)
    print(connection_of_airpot(graph,'Dallas'))


# To check the output of any function just remove the # sign
# exercise1()
# exercise2()
# exercise3()
exercise1()