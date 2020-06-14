from math import inf
from copy import copy,deepcopy
graph = {
    0: [1],
    1: [2, 6, 5],
    2: [3, 4],
    3: [2],
    4: [9],
    5: [4, 6, 8],
    6: [7],
    7: [8],
}
cost = {
    (0,1):5,
    (1,6):60,
    (1,2):20,
    (1,5):30,
    (2,3):10,
    (3,2):-15,
    (2,4):75,
    (4,9):100,
    (5,4):25,
    (5,6):5,
    (5,7):50,
    (5,8):50,
    (6,7):-50,
    (7,8):-10,
}

class Bellman():

    def __init__(self,graph,edges):
        self.graph = graph
        self.edges = edges
        self.nodes = set()
        self.dist = dict()
        self.dist_one = dict()
        self.dist_check = dict()

    def read_nodes(self):

        # writing all the nodes of the graph to self.nodes
        for key in graph.keys():
            self.nodes.add(key)
            for node in graph[key]:
                self.nodes.add(node)

        # creating dist to the each node = inf
        for n in self.nodes:
            self.dist[n] = inf

    def bellford(self,s):

        loop = 0
        # relaxing edges n-1 times
        while loop < len(self.nodes):
            # choosing proper distance in order to compare later and be able
            # to detect inf loops
            dist = self.dist

            visited = set()
            # checking the distances to all V
            dist[s] = 0
            for node in self.nodes:
                # check if the node has any neighbors
                if self.graph.get(node) is None:
                    continue
                for neighbor in self.graph[node]:
                    # if new dist is smaller, make new dist
                    if dist[neighbor]> dist[node] + self.edges[(node,neighbor)]:
                        dist[neighbor] = dist[node] + self.edges[(node, neighbor)]

            if loop == 0:
                self.dist_one = deepcopy(dist)
            else:
                self.dist_check = deepcopy(dist)
            loop += 1

        # detect nodes influenced by the inf loop
        for node in self.nodes:
            if self.dist_one[node]>self.dist_check[node]:
                self.dist[node] = - inf

bell = Bellman(graph,cost)
bell.read_nodes()
bell.bellford(0)
print(bell.dist)



