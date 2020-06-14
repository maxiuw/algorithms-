'''
finding the shortest path between all pairs of nodes APSP
'''
from math import inf
from copy import copy,deepcopy
import numpy as np
g = {
    1:[2,3],
    2:[1,4],
    3:[2],
    4:[3]
}
cost = {
    (1,2):9,
    (1,3):4,
    (2,1):-6,
    (2,4):2,
    (3,2):5,
    (4,3):1
}

class Floyd_Warshall():

    def __init__(self,graph,edges):
        self.graph = graph
        self.edges = edges
        self.nodes = set()
        self.matrix = None
        self.next = None

    # reading and creating a set of the nodes
    def read_nodes(self):

        # writing all the nodes of the graph to self.nodes
        for key in self.graph.keys():
            self.nodes.add(key)
            for node in self.graph[key]:
                self.nodes.add(node)

    def matrix_rep(self):
        # setting the matrix representation of the graph

        matrix_graph = np.zeros((len(self.nodes),len(self.nodes)))
        self.shortest_paths = np.zeros((len(self.nodes),len(self.nodes)))
        self.next = deepcopy(matrix_graph)
        # we could just loop for the elements but what if the elements are not
        # next numbers but tuples or letters ect

        for i in range(len(self.nodes)):
            for j in range(len(self.nodes)):
                if i == j:
                    matrix_graph[i][j] = 0

                elif self.graph.get(list(self.nodes)[i]) is not None:
                    if list(self.nodes)[j] in self.graph[list(self.nodes)[i]]:
                        matrix_graph[i][j] = self.edges[(list(self.nodes)[i],list(self.nodes)[j])]
                    else:
                        matrix_graph[i][j] = inf
                if matrix_graph[i][j]!= inf:
                    self.next[i][j] = j
                else:
                    matrix_graph[i][j] = inf

        self.matrix = matrix_graph

    def floydWar(self):
        # actual floyd-warshal for APSP

        for k in range(len(self.nodes)):
            for i in range(len(self.nodes)):
                if i==k:
                    continue
                for j in range(len(self.nodes)):
                    if j == k:
                        continue
                    if self.matrix[i][k] + self.matrix[k][j]<self.matrix[i][j]:
                        self.matrix[i][j] = self.matrix[i][k] + self.matrix[k][j]
                        self.next[i][j] = self.next[i][k]

        # detect negative cycles
        self.propagageNegativeCycles(self.matrix, len(self.nodes))

    def shortest(self,start,end):
        # print(self.nodes)
        path = []
        start = list(self.nodes)[list(self.nodes).index(start)]-1
        end =  list(self.nodes)[list(self.nodes).index(end)]-1
        # print(start,end)
        if self.matrix[start][end] == inf:
            return path

        node = start
        while end != node:
            if node == -1:
                return 'no path'
            path.append(node)

            node = int(self.next[node][end])
        path.append(end)
        # for the path to be an actual path, not indexes
        path = [i+1 for i in path]
        return path



    def propagageNegativeCycles(self,dp,n):

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    # print(dp[i][k] + dp[k][j])
                    # if there is a better path, improve the cost
                    if dp[i][k] + dp[k][j] < dp[i][j]:
                        dp[i][j] = - inf
                        self.shortest_paths[i][j] = -1


fw = Floyd_Warshall(graph=g, edges=cost)
fw.read_nodes()
fw.matrix_rep()
fw.floydWar()
print(fw.matrix)
print(fw.next)
print(fw.shortest(1,4))