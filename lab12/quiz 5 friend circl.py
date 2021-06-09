import ast

M = input()
M = ast.literal_eval(M)


def convertToAdjacencyList(M):
    G = {}
    for i in range(len(M)):
        G[i] = []

    for i in range(len(M)):
        for j in range(len(M)):
            if i != j and M[i][j] == 1:
                G[i].append(j)

    return G


def BFS(G, node):
    from queue import Queue
    queue = Queue()
    queue.put(node)
    visited = []
    while not queue.empty():
        vertex = queue.get()
        visited.append(vertex)
        for i in G[vertex]:
            if i not in visited:
                queue.put(i)
    return visited


def DFS(G, node, visit):
    visit.append(node)
    for edge in G[node]:
        if edge not in visit:
            DFS(G, edge, visit)
    return visit


def extractFriendCircles(M):
    graph = convertToAdjacencyList(M)
    temp = 0
    traversal_lst = []
    for i in graph:
        temp_lst = sorted(DFS(graph, i, []))
        if temp == 0:
            traversal_lst.append(temp_lst)
        else:
            if temp_lst not in traversal_lst:
                traversal_lst.append(temp_lst)
        temp += 1
    return traversal_lst


friendCircles = extractFriendCircles(M)
print(sorted(friendCircles, key=lambda x: x[0]))