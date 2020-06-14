from copy import copy
import numpy as np
from matplotlib import pyplot as plt
from seaborn import heatmap
# graph = {
#     1: [2, 3, 4],
#     2: [5, 6],
#     3: [10],
#     4: [7, 8],
#     5: [9, 10],
#     7: [11, 12],
#     11: [13]
# }

class Creator:


    def maze_creator(self,file):
        maze = open(file,'r',encoding="utf8")

        rows = 0
        array = np.array([[]])
        for line in maze:
            column = 0
            new_line = np.zeros([1, array.shape[1]])
            array = np.vstack((array, new_line))
            # print(array)
            for char in line:
                # adding new column to the array
                # print(array)
                if rows == 0 and column!=0:
                    array = np.column_stack((array, np.array([1])))

                elif rows==0 and column==0:
                    array = np.array([[0]])

                # 1 - field where we can mogve
                # 0 - blocked space
                if char.lower() == 's' or char.lower() == 'e' or char.lower() == ' ':

                    # saving start and exit to the memory
                    if char.lower()=='s':
                        start = (rows,column)
                    elif char.lower() =='e':
                        escape = (rows,column)
                    array[rows][column] = 1
                elif char=='█':
                    array[rows][column] = 0
                column += 1
                # array = np.column_stack((array, np.array([0])))

            rows += 1
        maze.close()
        return array,start,escape

    def graph_creator(self,maze):
        graph = dict()
        for i in range(maze.shape[0]):
            for j in range(maze.shape[1]):
                neighbours = []
                a=i
                for b in range(j - 1, j + 2):
                    if (a,b)!=(i,j) and a>=0 and b>=0 and a<maze.shape[0] and b < maze.shape[1] and maze[a][b]==1:
                        neighbours.append((a,b))
                b=j
                for a in range(i - 1, i + 2):
                    if (a,b)!=(i,j) and a>=0 and b>=0 and a<maze.shape[0] and b < maze.shape[1] and maze[a][b]==1:
                        neighbours.append((a,b))
                graph[(i,j)] = neighbours
        return graph

    # return graph,start,escape

class Solver(Creator):

    def bfs(self,graph,start,end):
        queue = []
        visited = set()
        # if end and start are the same

        if start == end:
            return start

        # adding starting point to the queue
        queue.append([start])

        while True:

            # check if there is already a solution path by checking the last element of the path
            # otherwise takes more time to get it and maybe the solution is already in the queue

            for paths in queue:
                if paths[-1]==end:
                    return paths
            if len(queue)==0:
                return 'there is no path'
            path = queue.pop(0)

            # adding the neighbour of the new node to the path
            if path[-1] not in visited:

                # if node doesnt have neighbors
                if graph.get(path[-1]) is None:
                    visited.add(path[-1])
                    continue

                # else create new paths with all possible neighbours
                for neighbour in graph[path[-1]]:
                    new_path = copy(path)
                    new_path.append(neighbour)
                    queue.append(new_path)

                visited.add(path[-1])

solver = Solver()

array = solver.maze_creator('maze.txt')
graph = solver.graph_creator(array[0])
solution = solver.bfs(graph,array[1],array[2])

# map = np.zeros([array[0].shape[0],array[0].shape[1]])
for path in solution:
    array[0][list(path)[0]][list(path)[1]]=10

plt.figure(figsize=(10,10))
heatmap(array[0],cmap='flag')
plt.show()

