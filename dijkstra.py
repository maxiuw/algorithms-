'''
This is the demo version, in a proper version of Dijkstra's algorithm the class Graph
should be used instead of dict, Can be used e.g. by networx library
'''

import numpy as np
import math
graph = {
    1: [2, 3, 4],
    2: [5, 6],
    3: [10],
    4: [7, 8],
    5: [9, 10],
    7: [11, 12],
    11: [13]
}
weights = dict()
nodes = set()
for key in graph.keys():
    nodes.add(key)
    for node in graph[key]:
        weights[(key,node)] = round(np.random.uniform(1,5),2)
        nodes.add(node)
graph = {**graph,**weights}
print(nodes)
print(weights)

class Dijkstra:

    def __init__(self,graph,nodes):
        self.graph = graph
        self.nodes = nodes # can be also extracted
        self.prev = dict()
        self.dist = dict()

    def dijkstra(self,graph,n,s):
        # they can be the lists but the thing is that later if the nodes
        # are more than 1d, we will have a problem so we change it for dic
        # but from the other hand, it s also bad since we dont know all the grah...
        visited = {i:False for i in n}
        dist = {i:math.inf for i in n}
        prev = {i:0 for i in n}
        dist[s] = 0

        # queue
        pq = []
        pq.append((s,0))

        while len(pq)!=0:
            index,minVal = pq.pop(0)
            visited[index] = True
            # if the value is of the node is already smaller, we dont care about it
            # we continue to the next node
            if dist[index]<minVal:
                continue

            # check if node has neighbours
            if graph.get(index) is None:
                continue
            for edge in graph[index]:
                # if neighbour was already visited, meaning there is a max value already...
                # idk for me it doesn't seem right...
                # print(edge)
                if visited[edge]:
                    continue
                # checking if new path is smaller than the previous one
                newDist = dist[index]+ graph[(index,edge)]
                if newDist<dist[edge]:
                    dist[edge] = newDist
                    # keeping track of to reproduce the path later
                    prev[edge] = index
                    pq.append((edge,newDist))

        # adding distances and previoously visted nodeds for the praticular starting point 's'
        self.prev[s] = prev
        self.dist[s] = dist

    def shortest_path(self,s,e):
        '''
        remember that if  path costs were not previously specify for the point s
        the path may be incorrect
        :param s: starting point
        :param e: ending point
        :return: path
        '''
        print(self.prev[s])
        node = e
        path = []
        while True:
            path.append(node)
            if node == s:
                return path[::-1]
            if self.prev[s][node]== 0 and node != s:
                return 'the path doesnt exist'
            node = self.prev[s][node]

d = Dijkstra(graph,nodes)
d.dijkstra(d.graph,d.nodes,1)
print(d.shortest_path(1,10))


